from datetime import datetime
import json
from pathlib import Path

neetcode_150 = {
    "Arrays & Hashing": [
        "Contains Duplicate",
        "Valid Anagram",
        "Two Sum",
        "Group Anagrams",
        "Top K Frequent Elements",
        "Encode and Decode Strings",
        "Product of Array Except Self",
        "Valid Sudoku",
        "Longest Consecutive Sequence",
        "Move Zeroes"
    ],
    "Two Pointers": [
        "Valid Palindrome",
        "Two Sum II Input Array Is Sorted",
        "3Sum",
        "Container With Most Water",
        "Trapping Rain Water"
    ],
    "Stack": [
        "Valid Parentheses",
        "Min Stack",
        "Evaluate Reverse Polish Notation",
        "Generate Parentheses",
        "Daily Temperatures",
        "Car Fleet",
        "Largest Rectangle in Histogram"
    ],
    "Binary Search": [
        "Binary Search",
        "Search a 2D Matrix",
        "Koko Eating Bananas",
        "Find Minimum in Rotated Sorted Array",
        "Search in Rotated Sorted Array",
        "Time Based Key Value Store",
        "Median of Two Sorted Arrays"
    ],
    "Sliding Window": [
        "Best Time to Buy and Sell Stock",
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Permutation in String",
        "Minimum Window Substring",
        "Sliding Window Maximum"
    ],
    "Linked List": [
        "Reverse Linked List",
        "Merge Two Sorted Lists",
        "Linked List Cycle",
        "Reorder List",
        "Remove Nth Node From End of List",
        "Copy List with Random Pointer",
        "Add Two Numbers",
        "Find The Duplicate Number",
        "LRU Cache",
        "Merge K Sorted Lists",
        "Reverse Nodes in K Group"
    ],
    "Trees": [
        "Invert Binary Tree",
        "Maximum Depth of Binary Tree",
        "Diameter of Binary Tree",
        "Balanced Binary Tree",
        "Same Tree",
        "Subtree of Another Tree",
        "Lowest Common Ancestor of A Binary Search Tree",
        "Binary Tree Level Order Traversal",
        "Binary Tree Right Side View",
        "Count Good Nodes in Binary Tree",
        "Validate Binary Search Tree",
        "Kth Smallest Element in a BST",
        "Construct Binary Tree from Preorder and Inorder Traversal",
        "Binary Tree Maximum Path Sum",
        "Serialize and Deserialize Binary Tree"
    ],
    "Tries": [
        "Implement Trie Prefix Tree",
        "Design Add and Search Words Data Structure",
        "Word Search II"
    ],
    "Heap / Priority Queue": [
        "Kth Largest Element in a Stream",
        "Last Stone Weight",
        "K Closest Points to Origin",
        "Kth Largest Element in an Array",
        "Task Scheduler",
        "Design Twitter",
        "Find Median from Data Stream"
    ],
    "Intervals": [
        "Insert Interval",
        "Merge Intervals",
        "Non Overlapping Intervals",
        "Meeting Rooms",
        "Meeting Rooms II",
        "Minimum Interval to Include Each Query"
    ],
    "Greedy": [
        "Maximum Subarray",
        "Jump Game",
        "Jump Game II",
        "Gas Station",
        "Hand of Straights",
        "Merge Triplets to Form Target Triplet",
        "Partition Labels",
        "Valid Parenthesis String"
    ],
    "Backtracking": [
        "Subsets",
        "Combination Sum",
        "Combination Sum II",
        "Permutations",
        "Subsets II",
        "Word Search",
        "Palindrome Partitioning",
        "Letter Combinations of a Phone Number",
        "N Queens"
    ],
    "Graphs": [
        "Number of Islands",
        "Max Area of Island",
        "Clone Graph",
        "Walls and Gates",
        "Rotting Oranges",
        "Pacific Atlantic Water Flow",
        "Surrounded Regions",
        "Course Schedule",
        "Course Schedule II",
        "Graph Valid Tree",
        "Number of Connected Components in an Undirected Graph",
        "Redundant Connection",
        "Word Ladder"
    ],
    "Advanced Graphs": [
        "Network Delay Time",
        "Reconstruct Itinerary",
        "Min Cost to Connect All Points",
        "Swim in Rising Water",
        "Alien Dictionary",
        "Cheapest Flights within K Stops",
    ],
    "1D Dynamic Programming": [
        "Climbing Stairs",
        "Min Cost Climbing Stairs",
        "House Robber",
        "House Robber II",
        "Longest Palindromic Substring",
        "Palindromic Substrings",
        "Decode Ways",
        "Coin Change",
        "Maximum Product Subarray",
        "Word Break",
        "Longest Increasing Subsequence",
        "Partition Equal Subset Sum"
    ],
    "2D Dynamic Programming": [
        "Unique Paths",
        "Longest Common Subsequence",
        "Best Time to Buy and Sell Stock with Cooldown",
        "Coin Change II",
        "Target Sum",
        "Interleaving String",
        "Longest Increasing Path in a Matrix",
        "Distinct Subsequences",
        "Edit Distance",
        "Burst Balloons",
        "Regular Expression Matching",
    ],
    "Bit Manipulation": [
        "Single Number",
        "Number of 1 Bits",
        "Counting Bits",
        "Reverse Bits",
        "Missing Number",
        "Sum of Two Integers",
        "Reverse Integer"
    ],
    "Math & Geometry": [
        "Rotate Image",
        "Spiral Matrix",
        "Set Matrix Zeroes",
        "Happy Number",
        "Plus One",
        "Powx n",
        "Multiply Strings",
        "Detect Squares"
    ]
}

base_uri = Path(__file__).parent
data_uri = base_uri.parent/"data"

def create_new_json(jsonfile: TextIOWrapper):
    with open(data_uri/"problems.txt") as readfile:
        res = {}
        for topic in neetcode_150:
            for problem in neetcode_150[topic]:
                res[problem] = {
                    'url': f"https://leetcode.com/problems/{'-'.join(problem.lower().split(' '))}",
                    'updated_datetime': datetime.now().isoformat(),
                    'revisit_date': None,
                    'count': 0,
                    'tag': topic
                }
        jsonfile.seek(0)
        json.dump(res, jsonfile, indent=4)
        jsonfile.truncate()