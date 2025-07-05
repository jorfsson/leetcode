import json
from io import TextIOWrapper
from argparse import ArgumentParser
from pathlib import Path

from datetime import datetime, timedelta
import regex
from sklearn.preprocessing import MinMaxScaler
import numpy as np



PROBLEMS = ['two-sum', 'add-two-numbers', 'longest-substring-without-repeating-characters', 'median-of-two-sorted-arrays', 'longest-palindromic-substring', 'coin-change-ii', 'reverse-integer', 'count-good-nodes-in-binary-tree', 'regular-expression-matching', 'container-with-most-water', 'rotting-oranges', '3sum', 'letter-combinations-of-a-phone-number', 'remove-nth-node-from-end-of-list', 'valid-parentheses', 'merge-two-sorted-lists', 'generate-parentheses', 'merge-k-sorted-lists', 'reverse-nodes-in-k-group', 'diameter-of-binary-tree', 'search-in-rotated-sorted-array', 'valid-sudoku', 'combination-sum', 'combination-sum-ii', 'trapping-rain-water', 'multiply-strings', 'jump-game-ii', 'permutations', 'rotate-image', 'group-anagrams', 'powx-n', 'n-queens', 'maximum-subarray', 'spiral-matrix', 'jump-game', 'merge-intervals', 'insert-interval', 'permutation-in-string', 'subtree-of-another-tree', 'unique-paths', 'plus-one', 'climbing-stairs', 'edit-distance', 'set-matrix-zeroes', 'search-a-2d-matrix', 'minimum-window-substring', 'subsets', 'word-search', 'largest-rectangle-in-histogram', 'subsets-ii', 'decode-ways', 'detect-squares', 'interleaving-string', 'validate-binary-search-tree', 'same-tree', 'binary-tree-level-order-traversal', 'last-stone-weight', 'maximum-depth-of-binary-tree', 'construct-binary-tree-from-preorder-and-inorder-traversal', 'task-scheduler', 'balanced-binary-tree', 'distinct-subsequences', 'best-time-to-buy-and-sell-stock', 'binary-tree-maximum-path-sum', 'valid-palindrome', 'word-ladder', 'longest-consecutive-sequence', 'surrounded-regions', 'palindrome-partitioning', 'clone-graph', 'gas-station', 'palindromic-substrings', 'single-number', 'copy-list-with-random-pointer', 'word-break', 'linked-list-cycle', 'reorder-list', 'lru-cache', 'evaluate-reverse-polish-notation', 'maximum-product-subarray', 'find-minimum-in-rotated-sorted-array', 'min-stack', 'valid-parenthesis-string', 'two-sum-ii-input-array-is-sorted', 'min-cost-to-connect-all-points', 'redundant-connection', 'max-area-of-island', 'reverse-bits', 'number-of-1-bits', 'house-robber', 'binary-tree-right-side-view', 'number-of-islands', 'happy-number', 'reverse-linked-list', 'course-schedule', 'implement-trie-prefix-tree', 'course-schedule-ii', 'design-add-and-search-words-data-structure', 'word-search-ii', 'house-robber-ii', 'kth-largest-element-in-an-array', 'contains-duplicate', 'invert-binary-tree', 'daily-temperatures', 'longest-common-subsequence', 'kth-smallest-element-in-a-bst', 'network-delay-time', 'lowest-common-ancestor-of-a-binary-search-tree', 'min-cost-climbing-stairs', 'product-of-array-except-self', 'sliding-window-maximum', 'valid-anagram', 'meeting-rooms', 'meeting-rooms-ii', 'partition-labels', 'graph-valid-tree', 'missing-number', 'alien-dictionary', 'encode-and-decode-strings', 'kth-largest-element-in-a-stream', 'binary-search', 'swim-in-rising-water', 'walls-and-gates', 'find-the-duplicate-number', 'cheapest-flights-within-k-stops', 'find-median-from-data-stream', 'serialize-and-deserialize-binary-tree', 'longest-increasing-subsequence', 'best-time-to-buy-and-sell-stock-with-cooldown', 'burst-balloons', 'coin-change', 'number-of-connected-components-in-an-undirected-graph', 'longest-increasing-path-in-a-matrix', 'reconstruct-itinerary', 'counting-bits', 'top-k-frequent-elements', 'design-twitter', 'hand-of-straights', 'sum-of-two-integers', 'car-fleet', 'koko-eating-bananas', 'partition-equal-subset-sum', 'pacific-atlantic-water-flow', 'longest-repeating-character-replacement', 'non-overlapping-intervals', 'minimum-interval-to-include-each-query', 'merge-triplets-to-form-target-triplet', 'target-sum', 'k-closest-points-to-origin', 'time-based-key-value-store']

parser = ArgumentParser()
parser.add_argument('--completed', action='store', dest='completed', type=str)
parser.add_argument('--get-problem', action='store_true', dest='get_problem')
parser.add_argument('--get-count', action='store', dest='get_count', type=str)
parser.add_argument('--reset', action='store_true', dest='reset')


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
            print(f'{problem} not found.')
            print("Possible matches:")
            print(self.search(problem))
            return
        
        self._problems[problem]['count'] += 1
        self._problems[problem]['updated_time'] = datetime.now().isoformat()
        self._problems[problem]['revisit_date'] = self._get_next_revisit_date(self._problems[problem]['count'])
        self._update_data()
        return self._problems[problem]['count']
    
    def _get_next_revisit_date(self, count: int) -> datetime.date:
        days = [1, 3, 7, 14, 30, 60, 90]
        if count < len(days):
            return (datetime.now().date() + timedelta(days=days[count - 1])).isoformat()
        return (datetime.now().date() + timedelta(days=90)).isoformat()

    def get_count(self, problem: str) -> int:
        if problem not in self._problems:
            print(f'{problem} not found.')
            print("Possible matches:")
            print(self.search(problem))
            return
        return self._problems[problem]['count']
    
    def get_next_problem(self) -> str:
        elements = [self._problems[e] for e in self._problems]
        elements.sort(key=lambda x: x.get('revisit_date', datetime.now().date()))
        
        for e in elements:
            if 'revisit_date' in e and e['revisit_date'] <= datetime.now().date():
                print(e['url'])
                return
        for e in elements:
            if 'revisit_date' not in e:
                print(e['url'])
                return
        print("No problems available for revisiting today.")
    
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

def create_new_json(jsonfile: TextIOWrapper):
    with open(data_uri/"problems.txt") as readfile:
        res = {}
        for line in readfile:
            name = line.split('/')[-1]
            res[name] = {
                'url': line.strip(),
                'updated_datetime': datetime.now().isoformat(),
                'count': 0
            }
        jsonfile.seek(0)
        json.dump(res, jsonfile, indent=4)
        jsonfile.truncate()

def main():
    with open(data_uri/'problems.json', 'r+') as jsonfile:
        leetcode = LeetCode(jsonfile)
        if args.reset:
            create_new_json(jsonfile)
        if args.get_count:
            leetcode.get_count(args.get_count)
        if args.get_problem:
            leetcode.get_next_problem()
        if args.completed:
            leetcode.increment_count(args.completed)

if __name__ == "__main__":
    main()
