import json
from io import TextIOWrapper
from datetime import datetime
from typing import Dict, Generator, List, Optional, Tuple, Union
import regex

from .spaced_repetition import SpacedRepetition


class ProblemManager:
    """Manages LeetCode problem tracking and retrieval"""

    def __init__(self, data: TextIOWrapper):
        """
        Initialize the problem manager.

        Args:
            data: File handle to problems.json
        """
        self._data = data
        self._problems: Dict[str, dict] = json.load(self._data)

    def _update_data(self) -> None:
        """Write current problem state back to JSON file"""
        self._data.seek(0)
        json.dump(self._problems, self._data, indent=4)
        self._data.truncate()

    def search(self, problem: str) -> Optional[Union[str, List[str]]]:
        """
        Search for a problem using exact match, normalized match, or fuzzy matching.

        Args:
            problem: Problem name to search for

        Returns:
            - Exact match: problem name (str)
            - Fuzzy match: list of matching problem names
            - No match: None
        """
        # First try exact match
        if problem in self._problems:
            return problem

        # Normalize input: replace underscores with hyphens
        normalized_problem = problem.replace('_', '-').lower()

        # Try normalized exact match
        if normalized_problem in self._problems:
            return normalized_problem

        # Fuzzy match using regex module with error tolerance
        # Allow 1-2 character differences for fuzzy matching
        fuzzy_pattern = regex.compile(f"({regex.escape(normalized_problem)}){{e<=2}}", regex.IGNORECASE)

        matches = []
        for key in self._problems.keys():
            match = fuzzy_pattern.search(key)
            if match:
                matches.append((key, match))

        if matches:
            # Sort by match quality (shorter distance is better)
            matches.sort(key=lambda x: len(x[0]))
            return [match[0] for match in matches]

        print(f"No match found for '{problem}'")
        return None

    def increment_count(self, problem: str) -> int:
        """
        Mark a problem as completed and update its revisit date.

        Args:
            problem: Problem name

        Returns:
            Updated completion count

        Raises:
            ValueError: If problem not found
        """
        if problem not in self._problems:
            raise ValueError(f'{problem} not found.')

        self._problems[problem]['revisit_date'] = SpacedRepetition.get_next_revisit_date(
            self._problems[problem]['count']
        )
        self._problems[problem]['count'] += 1
        self._problems[problem]['updated_datetime'] = datetime.now().isoformat()
        self._update_data()
        return self._problems[problem]['count']

    def get_next_problem(self) -> Generator[Tuple[str, dict], None, None]:
        """
        Yield problems in priority order:
        1. Problems due for revisit
        2. Uncompleted problems

        Yields:
            Tuple of (problem_name, problem_data)
        """
        problems_to_revisit = {
            k: v for k, v in self._problems.items()
            if SpacedRepetition.is_due_for_review(v.get('revisit_date'))
        }
        uncompleted_problems = {
            k: v for k, v in self._problems.items()
            if not v.get('revisit_date')
        }

        for k, v in problems_to_revisit.items():
            yield k, v
        for k, v in uncompleted_problems.items():
            yield k, v

    def add_problem(self, problem: str, tag: str) -> None:
        """
        Add a new problem to the tracking system.

        Args:
            problem: Problem name
            tag: Category tag for the problem
        """
        if problem in self._problems:
            print(f"{problem} already exists.")
            return

        self._problems[problem] = {
            'url': f"https://leetcode.com/problems/{'-'.join(problem.lower().split(' '))}",
            'updated_datetime': datetime.now().isoformat(),
            'revisit_date': None,
            'count': 0,
            'tag': tag
        }
        self._update_data()
        print(f"Added {problem}.")

    def get_count(self, problem: str) -> int:
        """
        Get the completion count for a problem.

        Args:
            problem: Problem name (supports fuzzy matching)

        Returns:
            Completion count

        Raises:
            ValueError: If problem not found
        """
        if problem not in self._problems:
            # Try fuzzy search
            match = self.search(problem)
            if match:
                if isinstance(match, list):
                    problem = match[0]
                else:
                    problem = match
            else:
                raise ValueError(f'{problem} not found.')
        return self._problems[problem]['count']

    def reset(self, neetcode_150: Dict[str, List[str]]) -> None:
        """
        Reset all problems to default state.

        Args:
            neetcode_150: Dictionary of problem categories and names
        """
        for topic in neetcode_150:
            for problem in neetcode_150[topic]:
                self._problems[problem] = {
                    'url': f"https://leetcode.com/problems/{'-'.join(problem.lower().split(' '))}",
                    'updated_datetime': datetime.now().isoformat(),
                    'revisit_date': None,
                    'count': 0,
                    'tag': topic
                }
        self._update_data()
        print("Problems database reset to default state.")
