# Stacks

## Monotonic Stacks
Increasing vs decreasing
Strictly vs non-strictly

### Sum of Subarray Minimums

**Problem:** *Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.*

*Brute Force*
Time complexity: O(n)^2
`
res = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr) + 1):
        res += min(arr[i:j])
return res
`

*Monotonic Stack*
Notes:
- Re-orient perspective - what subarrays for the current value is it the min?
- Given a range, how do you calculate all subarrays that contain the current value?
  - Given a range, all combinations of subarrays for a current value include all combinations of values to the left of the current value as the start and all values to the right of the current value as the end
  - Number of values on left * number of values on the right
  - (i - 1) * (n - i)