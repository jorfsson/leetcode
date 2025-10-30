import json
from io import TextIOWrapper
from argparse import ArgumentParser
from pathlib import Path

from datetime import datetime, timedelta
import regex
from sklearn.preprocessing import MinMaxScaler
import numpy as np


parser = ArgumentParser()
parser.add_argument('--completed', action='store', dest='completed', type=str)
parser.add_argument('--get-problem', action='store_true', dest='get_problem')
parser.add_argument('--add-problem', action='store', dest='add_problem', nargs=2)

args = parser.parse_args()
base_uri = Path(__file__).parent
data_uri = base_uri.parent/"data"

class LeetCode:
    def __init__(self, data: TextIOWrapper):
        self._data = data
        self._problems = json.load(self._data)

    def _update_data(self):
        self._data.seek(0)
        json.dump(self._problems, self._data, indent=4)
        self._data.truncate()

    def search(self, problem: str) -> str:
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
        if problem not in self._problems:
            raise ValueError(f'{problem} not found.')
        self._problems[problem]['revisit_date'] = self._get_next_revisit_date(self._problems[problem]['count'])
        self._problems[problem]['count'] += 1
        self._problems[problem]['updated_time'] = datetime.now().isoformat()
        self._update_data()
        return self._problems[problem]['count']
    
    def _get_next_revisit_date(self, count: int) -> datetime.date:
        days = [1, 3, 7, 14, 30, 60, 90]
        if count < len(days):
            return (datetime.now().date() + timedelta(days=days[count])).isoformat()
        return (datetime.now().date() + timedelta(days=90)).isoformat()
    
    def get_next_problem(self):
        problems_to_revisit = {k: v for k, v in self._problems.items() if v['revisit_date'] and datetime.strptime(v['revisit_date'], "%Y-%m-%d").date() <= datetime.now().date()}
        uncompleted_problems = {k: v for k, v in self._problems.items() if not v['revisit_date']}
        
        for k, v in problems_to_revisit.items():
            yield k, v
        for k, v in uncompleted_problems.items():
            yield k, v

    def get_random_problem(self):
        elements = [self._problems[e] for e in self._problems]
        counts = np.array([[e["count"]] for e in elements])
        recencies = np.array([[-self._get_timedelta(e['updated_datetime'])] for e in elements]) 

        scaler = MinMaxScaler()
        norm_counts = scaler.fit_transform(counts)
        norm_recencies = scaler.fit_transform(recencies)

        α, β = 0.7, 0.3  # Example weights

        for i, e in enumerate(elements):
            e["score"] = α * norm_counts[i][0] + β * norm_recencies[i][0]

        elements.sort(key=lambda x: x["score"], reverse=True)

        return elements[0]['url']
    
    def _get_timedelta(self, updated_datetime: str) -> datetime:
        now = datetime.now()
        return (now - datetime.fromisoformat(updated_datetime)).total_seconds()
    
    def add_problem(self, problem: str, tag: str):
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

def main():
    with open(data_uri/'problems.json', 'r+') as jsonfile:
        leetcode = LeetCode(jsonfile)
        if args.get_problem:
            for k, v in leetcode.get_next_problem():
                print(v['url'])
                res = input()
                match res:
                    case 'completed':
                        leetcode.increment_count(k)
                    case 'exit':
                        return
                    case _:
                        continue
        if args.add_problem:
            leetcode.add_problem(args.add_problem[0], args.add_problem[1])
  
        if args.completed:
            leetcode.increment_count(args.completed)

if __name__ == "__main__":
    main()
