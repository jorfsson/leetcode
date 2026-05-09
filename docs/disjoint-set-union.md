# Disjoint Set Union (Union Find)

## Core Concept
A data structure for tracking a collection of elements partitioned into disjoint (non-overlapping) sets. Supports two operations efficiently:
- **Union** — merge two sets into one
- **Find** — identify which set an element belongs to (returns the set's representative/root)

Sets are stored as trees. Each element points to a parent; the root of each tree is the representative of that set.

## Key Patterns

### Basic Implementation
```python
parent = list(range(n))  # each node is its own parent initially
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return False  # already in same set
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px  # union by rank
    if rank[px] == rank[py]:
        rank[px] += 1
    return True
```

### Optimizations
- **Path compression** — during Find, make every node on the path point directly to the root; flattens the tree over time
- **Union by rank** — always attach the shorter tree under the taller one; keeps tree height logarithmic

Together these give near-constant amortized time: O(α(n)) per operation where α is the inverse Ackermann function.

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
