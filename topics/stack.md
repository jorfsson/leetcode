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
