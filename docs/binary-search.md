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
