# Study Plan

**Goal:** Crack hard-level problems across all NeetCode 150 categories  
**Timeline:** 8 weeks  
**Approach:** Depth-first by dependency order — master each category's patterns before moving to ones that build on it

---

## Category Sequence

1. **Binary Search** — finish what's started; boundary patterns appear everywhere
2. **Sliding Window** — self-contained; builds variable-window intuition used in DP later
3. **Linked List** — self-contained; pointer manipulation fluency needed for Trees
4. **Trees** — largest category (15 problems); unlocks Tries, Heap, and Graph intuition
5. **Tries** — tree variant; natural follow-on while tree patterns are fresh
6. **Heap / Priority Queue** — tree-backed structure; k-element and streaming patterns
7. **Backtracking** — state-space search; builds the intuition behind DP's subproblem decomposition
8. **Graphs** — BFS/DFS at scale; builds on tree traversal
9. **Advanced Graphs** — Dijkstra, Prim, Kruskal, topological sort; depends on Graphs
10. **Greedy** — local-optimum reasoning; easier after seeing graph/interval problems
11. **Intervals** — overlap detection; pairs well with Greedy
12. **1D Dynamic Programming** — subproblem decomposition; hardest conceptual shift
13. **2D Dynamic Programming** — builds directly on 1D DP intuition
14. **Bit Manipulation** — interleave anytime; low dependency, good for rest days
15. **Math & Geometry** — interleave anytime; low dependency, good for rest days

---

## Weekly Schedule

| Week | Categories | Problems |
|------|-----------|---------|
| 1 | Binary Search (finish) + Sliding Window | 6 + 6 = 12 |
| 2 | Linked List | 11 |
| 3–4 | Trees | 15 |
| 5 | Tries + Heap / Priority Queue | 3 + 7 = 10 |
| 6 | Backtracking + Graphs (start) | 9 + 6 |
| 7 | Graphs (finish) + Advanced Graphs | 7 + 6 |
| 7–8 | Greedy + Intervals | 8 + 6 = 14 |
| 8 | 1D DP + 2D DP | 12 + 11 |
| ongoing | Bit Manipulation + Math & Geometry | 7 + 8 = 15 |

---

## Per-Category Problem Priorities

Problems that best teach the hard-level patterns for each category.

### Binary Search
- **Median of Two Sorted Arrays** — binary search on two arrays; hardest problem in the category
- **Koko Eating Bananas** — binary search on answer space, not array index
- **Search in Rotated Sorted Array** — handling the pivot break in invariant reasoning

### Sliding Window
- **Minimum Window Substring** — variable window with character frequency tracking
- **Sliding Window Maximum** — monotonic deque; hard variant of the pattern
- **Longest Repeating Character Replacement** — window validity condition is non-obvious

### Linked List
- **Reverse Nodes in K Group** — recursive pointer manipulation at hard level
- **Merge K Sorted Lists** — heap-based merge; bridges into Heap category
- **LRU Cache** — doubly linked list + hashmap design; common hard design problem

### Trees
- **Serialize and Deserialize Binary Tree** — full tree reconstruction; hard design problem
- **Binary Tree Maximum Path Sum** — global max tracking through recursive returns
- **Construct Binary Tree from Preorder and Inorder Traversal** — index reasoning across two arrays

### Tries
- **Word Search II** — trie + backtracking combined; teaches when to reach for a trie
- **Design Add and Search Words Data Structure** — wildcard matching through trie nodes

### Heap / Priority Queue
- **Find Median from Data Stream** — two-heap balancing; canonical hard heap problem
- **Task Scheduler** — greedy + frequency heap; bridges into Greedy category
- **Design Twitter** — k-way merge with heap; combines design + heap reasoning

### Backtracking
- **N Queens** — constraint propagation with backtracking; canonical hard
- **Word Search** — 2D grid backtracking with visited tracking
- **Palindrome Partitioning** — backtracking with memoizable subproblems; bridges into DP

### Graphs
- **Word Ladder** — BFS on implicit graph; hardest BFS problem
- **Course Schedule II** — topological sort; prerequisite for Advanced Graphs
- **Pacific Atlantic Water Flow** — multi-source BFS/DFS; non-obvious direction reversal

### Advanced Graphs
- **Alien Dictionary** — topological sort on inferred graph; hard reasoning problem
- **Swim in Rising Water** — Dijkstra variant; bridges shortest-path to binary search on answer
- **Reconstruct Itinerary** — Eulerian path with backtracking; hard graph + ordering problem

### Greedy
- **Jump Game II** — greedy interval expansion; non-obvious why greedy works
- **Gas Station** — greedy with circular invariant reasoning
- **Valid Parenthesis String** — greedy range tracking; bridges into DP

### Intervals
- **Minimum Interval to Include Each Query** — heap + offline query processing; hardest in category
- **Meeting Rooms II** — classic interval scheduling; foundation for the rest
- **Non Overlapping Intervals** — greedy interval removal; teaches the core overlap pattern

### 1D Dynamic Programming
- **Word Break** — DP on string segmentation; non-obvious state definition
- **Longest Increasing Subsequence** — O(n log n) patience sorting variant is the hard version
- **Partition Equal Subset Sum** — subset sum DP; bridges into 2D DP

### 2D Dynamic Programming
- **Regular Expression Matching** — hardest problem in the set; state machine + DP
- **Burst Balloons** — interval DP; requires thinking backwards
- **Edit Distance** — canonical 2D DP; teaches the grid-filling pattern

### Bit Manipulation
- **Sum of Two Integers** — addition without `+`; teaches carry propagation with XOR/AND
- **Reverse Integer** — overflow handling; deceptively tricky

### Math & Geometry
- **Multiply Strings** — grade-school multiplication in code; tests implementation precision
- **Pow(x, n)** — fast exponentiation; O(log n) divide-and-conquer
