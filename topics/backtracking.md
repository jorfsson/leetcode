# Backtracking

## Core Concept
Make a choice
Explore consequences
Undo the choice
Try another choice


def dfs(start, path):
    for i in range(start, n):
        choose(i)
        dfs(i + 1, curr)wwwww
        unchoose(i)

## Key Patterns
**Enumeration**: Visit every possible combination of choices; generate all states.
**Target Search**: Find paths satisfying a constraint; search for feasible solutions.
**Permutation Search**: Produce all possible orderings; use a set.

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
