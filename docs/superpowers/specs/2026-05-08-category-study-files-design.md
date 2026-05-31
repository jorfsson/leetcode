# Category Study Files — Design Spec

**Date:** 2026-05-08

---

## Problem Statement

The LeetCode tracker surfaces what problem to do next, but provides no structured place to record *why* a category works the way it does — the core concepts, patterns, gotchas, and which problems illuminate which ideas. The existing `docs/` files (binary-search.md, stacks.md, disjoint-set-union.md) do this informally but inconsistently.

---

## Goal

Create a consistent set of category-level study files in `docs/` — one per NeetCode 150 category — that serve as living documents. They get richer both during spaced repetition sessions (adding a problem insight after working it) and during independent study.

---

## File Structure

One markdown file per NeetCode category, named as a lowercase hyphenated slug derived from the category name:

| Category | File |
|---|---|
| Arrays & Hashing | `docs/arrays-and-hashing.md` |
| Two Pointers | `docs/two-pointers.md` |
| Stack | `docs/stack.md` |
| Binary Search | `docs/binary-search.md` |
| Sliding Window | `docs/sliding-window.md` |
| Linked List | `docs/linked-list.md` |
| Trees | `docs/trees.md` |
| Tries | `docs/tries.md` |
| Heap / Priority Queue | `docs/heap-priority-queue.md` |
| Intervals | `docs/intervals.md` |
| Greedy | `docs/greedy.md` |
| Backtracking | `docs/backtracking.md` |
| Graphs | `docs/graphs.md` |
| Advanced Graphs | `docs/advanced-graphs.md` |
| 1D Dynamic Programming | `docs/1d-dynamic-programming.md` |
| 2D Dynamic Programming | `docs/2d-dynamic-programming.md` |
| Bit Manipulation | `docs/bit-manipulation.md` |
| Math & Geometry | `docs/math-and-geometry.md` |
| Disjoint Set Union | `docs/disjoint-set-union.md` |

Slug rules: lowercase, `&` → `and`, `/` → `-`, spaces → `-`, strip other special chars.

---

## File Template

Each file follows this exact structure:

```markdown
# <Category Name>

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

All sections start empty (comments only) except the heading. The user fills them in over time.

---

## Migration of Existing Files

Three files already exist with freeform content. Their content must be preserved and slotted into the appropriate sections of the new structure:

- `docs/binary-search.md` — content fits under **Key Patterns** (boundary types) and **Common Gotchas** (termination conditions)
- `docs/stacks.md` — content to be slotted into appropriate sections
- `docs/disjoint-set-union.md` — already exists; migrate freeform content into the new template structure. DSU is kept as its own standalone file even though it is not a NeetCode category, as it is a distinct enough data structure to warrant its own document.

---

## What Is Not In Scope

- No skill or CLI command for scaffolding — files are created once as part of this implementation
- No automation linking `--get-problem` output to the relevant category file (can be added later)
- No per-problem files — insights live as bullets in the category file's Problems section
- No template file on disk — the structure is the convention, applied consistently by the implementer

---

## Success Criteria

- All 19 files exist in `docs/` (18 NeetCode categories + DSU) with correct slugs and consistent section structure
- Existing content from the 3 migrated files is preserved and placed in the correct sections
- `docs/stacks.md` is renamed/replaced by `docs/stack.md` to match the category slug
- `docs/disjoint-set-union.md` is migrated to the new template structure (not merged elsewhere)
