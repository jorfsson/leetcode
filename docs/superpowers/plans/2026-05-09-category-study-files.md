# Category Study Files Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create 19 structured markdown study files in `docs/` — one per NeetCode 150 category plus DSU — and migrate the 3 existing freeform files into the new consistent template structure.

**Architecture:** All files are pure markdown, no code changes. Each file follows a fixed 5-section template (Core Concept, Key Patterns, When to Recognize It, Common Gotchas, Problems). New files start with empty sections; existing files have their content slotted into the appropriate sections.

**Tech Stack:** Markdown, git

---

## File Map

**Create (new, empty template):**
- `docs/arrays-and-hashing.md`
- `docs/two-pointers.md`
- `docs/sliding-window.md`
- `docs/linked-list.md`
- `docs/trees.md`
- `docs/tries.md`
- `docs/heap-priority-queue.md`
- `docs/intervals.md`
- `docs/greedy.md`
- `docs/backtracking.md`
- `docs/graphs.md`
- `docs/advanced-graphs.md`
- `docs/1d-dynamic-programming.md`
- `docs/2d-dynamic-programming.md`
- `docs/bit-manipulation.md`
- `docs/math-and-geometry.md`

**Migrate (rewrite with template, preserving content):**
- `docs/binary-search.md` — existing content → Key Patterns + Common Gotchas
- `docs/stack.md` — replaces `docs/stacks.md`; existing content → Key Patterns + Problems
- `docs/disjoint-set-union.md` — existing content → Core Concept + Key Patterns

**Delete:**
- `docs/stacks.md` (replaced by `docs/stack.md`)

---

### Task 1: Migrate `docs/binary-search.md`

**Files:**
- Modify: `docs/binary-search.md`

Current content covers boundary types (inclusive vs exclusive) and termination — these map to Key Patterns and Common Gotchas respectively.

- [ ] **Step 1: Rewrite `docs/binary-search.md` with template structure**

Replace the entire file with:

```markdown
# Binary Search

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns

### Search Boundaries
Two boundary styles determine loop condition and pointer updates:

- **Inclusive `[low, high]`** — both endpoints are valid candidates
  - Loop condition: `l <= r`
  - Update left: `l = mid + 1`
  - Update right: `r = mid - 1`
- **Exclusive `[low, high)`** — high is never a valid candidate
  - Loop condition: `l < r`
  - Update left: `l = mid + 1`
  - Update right: `r = mid`

### Finding Values vs Finding Boundaries
Binary search is used for two distinct purposes:
- **Finding a value** — searching for an exact target in a sorted array
- **Finding a boundary** — searching for the point where a condition flips (e.g. first index where `arr[i] >= target`)

Boundary problems often use exclusive style because the answer may be at `high`.

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas

### Termination
- `[low, high]` terminates when `low > high` (interval is empty)
- `[low, high)` terminates when `low == high` (interval is empty)

Mixing these up causes infinite loops or missed elements.

### Midpoint Overflow
Use `mid = low + (high - low) // 2` instead of `(low + high) // 2` to avoid integer overflow in languages with fixed-width integers.

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 2: Verify file looks correct**

```bash
cat docs/binary-search.md
```

Expected: file has all 5 sections, original boundary content preserved under Key Patterns and Common Gotchas.

- [ ] **Step 3: Commit**

```bash
git add docs/binary-search.md
git commit -m "docs: migrate binary-search.md to template structure"
```

---

### Task 2: Migrate `docs/stacks.md` → `docs/stack.md`

**Files:**
- Create: `docs/stack.md`
- Delete: `docs/stacks.md`

Current content covers monotonic stacks with a worked example (Sum of Subarray Minimums) — maps to Key Patterns and Problems.

- [ ] **Step 1: Create `docs/stack.md` with template structure**

```markdown
# Stack

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns

### Monotonic Stacks
A stack that maintains elements in strictly increasing or decreasing order. When a new element violates the order, pop until the invariant is restored.

Variants:
- **Increasing** — each element is greater than the one below it; useful for finding next smaller element
- **Decreasing** — each element is smaller than the one below it; useful for finding next greater element
- **Strictly vs non-strictly monotonic** — determines whether equal elements are allowed

**Key insight for sum-of-subarray problems:** Re-orient perspective. Instead of asking "what is the min of this subarray?", ask "for which subarrays is the current element the minimum?" Given a value at index `i` with `left` elements to its left and `right` elements to its right where it is the minimum:
- Number of subarrays where it is the min = `left * right`
- Use a monotonic stack to find the left and right boundaries efficiently

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems

- **Sum of Subarray Minimums** — monotonic stack to find, for each element, how many subarrays it is the minimum of; count = `(i - left_boundary) * (right_boundary - i)`
```

- [ ] **Step 2: Delete `docs/stacks.md`**

```bash
git rm docs/stacks.md
```

- [ ] **Step 3: Verify**

```bash
ls docs/stack* && cat docs/stack.md
```

Expected: `docs/stack.md` exists, `docs/stacks.md` does not.

- [ ] **Step 4: Commit**

```bash
git add docs/stack.md
git commit -m "docs: migrate stacks.md → stack.md with template structure"
```

---

### Task 3: Migrate `docs/disjoint-set-union.md`

**Files:**
- Modify: `docs/disjoint-set-union.md`

Current content covers the definition, tree representation, and two operations (Union, Find — Find is incomplete).

- [ ] **Step 1: Rewrite `docs/disjoint-set-union.md` with template structure**

```markdown
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
```

- [ ] **Step 2: Verify**

```bash
cat docs/disjoint-set-union.md
```

Expected: all 5 sections present, original Core Concept and Key Patterns content preserved and expanded.

- [ ] **Step 3: Commit**

```bash
git add docs/disjoint-set-union.md
git commit -m "docs: migrate disjoint-set-union.md to template structure"
```

---

### Task 4: Create new category files — Group 1 (Arrays through Sliding Window)

**Files:**
- Create: `docs/arrays-and-hashing.md`
- Create: `docs/two-pointers.md`
- Create: `docs/sliding-window.md`

- [ ] **Step 1: Create `docs/arrays-and-hashing.md`**

```markdown
# Arrays & Hashing

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 2: Create `docs/two-pointers.md`**

```markdown
# Two Pointers

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 3: Create `docs/sliding-window.md`**

```markdown
# Sliding Window

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 4: Commit**

```bash
git add docs/arrays-and-hashing.md docs/two-pointers.md docs/sliding-window.md
git commit -m "docs: add arrays-and-hashing, two-pointers, sliding-window study files"
```

---

### Task 5: Create new category files — Group 2 (Linked List through Intervals)

**Files:**
- Create: `docs/linked-list.md`
- Create: `docs/trees.md`
- Create: `docs/tries.md`
- Create: `docs/heap-priority-queue.md`
- Create: `docs/intervals.md`

- [ ] **Step 1: Create `docs/linked-list.md`**

```markdown
# Linked List

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 2: Create `docs/trees.md`**

```markdown
# Trees

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 3: Create `docs/tries.md`**

```markdown
# Tries

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 4: Create `docs/heap-priority-queue.md`**

```markdown
# Heap / Priority Queue

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 5: Create `docs/intervals.md`**

```markdown
# Intervals

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 6: Commit**

```bash
git add docs/linked-list.md docs/trees.md docs/tries.md docs/heap-priority-queue.md docs/intervals.md
git commit -m "docs: add linked-list, trees, tries, heap-priority-queue, intervals study files"
```

---

### Task 6: Create new category files — Group 3 (Greedy through Advanced Graphs)

**Files:**
- Create: `docs/greedy.md`
- Create: `docs/backtracking.md`
- Create: `docs/graphs.md`
- Create: `docs/advanced-graphs.md`

- [ ] **Step 1: Create `docs/greedy.md`**

```markdown
# Greedy

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 2: Create `docs/backtracking.md`**

```markdown
# Backtracking

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 3: Create `docs/graphs.md`**

```markdown
# Graphs

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 4: Create `docs/advanced-graphs.md`**

```markdown
# Advanced Graphs

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 5: Commit**

```bash
git add docs/greedy.md docs/backtracking.md docs/graphs.md docs/advanced-graphs.md
git commit -m "docs: add greedy, backtracking, graphs, advanced-graphs study files"
```

---

### Task 7: Create new category files — Group 4 (DP through Math & Geometry)

**Files:**
- Create: `docs/1d-dynamic-programming.md`
- Create: `docs/2d-dynamic-programming.md`
- Create: `docs/bit-manipulation.md`
- Create: `docs/math-and-geometry.md`

- [ ] **Step 1: Create `docs/1d-dynamic-programming.md`**

```markdown
# 1D Dynamic Programming

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 2: Create `docs/2d-dynamic-programming.md`**

```markdown
# 2D Dynamic Programming

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 3: Create `docs/bit-manipulation.md`**

```markdown
# Bit Manipulation

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 4: Create `docs/math-and-geometry.md`**

```markdown
# Math & Geometry

## Core Concept
<!-- What is this category fundamentally about? What problem class does it solve? -->

## Key Patterns
<!-- Recurring techniques and approaches used across problems in this category -->

## When to Recognize It
<!-- Signals in a problem statement that suggest this category applies -->

## Common Gotchas
<!-- Non-obvious traps, edge cases, off-by-one errors specific to this category -->

## Problems
<!-- Problems mapped to the concept or pattern they exercise.
Format: **Problem Name** — what it teaches / which pattern it exercises -->
```

- [ ] **Step 5: Commit**

```bash
git add docs/1d-dynamic-programming.md docs/2d-dynamic-programming.md docs/bit-manipulation.md docs/math-and-geometry.md
git commit -m "docs: add 1d-dp, 2d-dp, bit-manipulation, math-and-geometry study files"
```

---

### Task 8: Final verification

- [ ] **Step 1: Confirm all 19 files exist**

```bash
ls docs/*.md | grep -v superpowers | sort
```

Expected output (19 files):
```
docs/1d-dynamic-programming.md
docs/2d-dynamic-programming.md
docs/advanced-graphs.md
docs/arrays-and-hashing.md
docs/backtracking.md
docs/binary-search.md
docs/bit-manipulation.md
docs/disjoint-set-union.md
docs/graphs.md
docs/greedy.md
docs/heap-priority-queue.md
docs/intervals.md
docs/linked-list.md
docs/math-and-geometry.md
docs/sliding-window.md
docs/stack.md
docs/trees.md
docs/tries.md
docs/two-pointers.md
```

- [ ] **Step 2: Confirm `stacks.md` is gone**

```bash
ls docs/stacks.md 2>&1
```

Expected: `No such file or directory`

- [ ] **Step 3: Confirm all files have the 5 required sections**

```bash
for f in docs/*.md; do [[ "$f" == *superpowers* ]] && continue; echo "=== $f ==="; grep "^## " "$f"; done
```

Expected: every file shows `## Core Concept`, `## Key Patterns`, `## When to Recognize It`, `## Common Gotchas`, `## Problems`.
