# Quickselect

[Quickselect](https://en.wikipedia.org/wiki/Quickselect) implementations in Python, with testing available via `pytest`.  Used to sort values in an array (Python `list`) from lowest to highest.

Requirements:
- Input is an array
- Values in the array are sortable:  allow the `<` comparison operator

Edge Cases / Caveats:
- Empty array input
- Duplicate (equal) values
- Negative values
- Invalid `numbers` or values of `k`
- Recursion depth

Time complexity: `O(n)` average case, `O(n²)` worst case.

## Approach

Use a divide and conquer (D&C) strategy to break the problem down into reusable, recursive steps.  This works very much like `quicksort`, but with some differences.

Base cases:
1. `k < 1`: no answer -> `None`
2. `k == 1`: kth largest is the largest of current list
3. `len(numbers) < k`: no answer -> `None`
4. `len(numbers) == k`: kth largest is the lowest of current list

Recursive case:
1. divide and conquer at a random index (the *pivot*)
    - index `[0]` generally suffices as a random index
    - a central index `len(numbers) // 2` would be preferred if `numbers` is sorted
    - add pivot to end of LHS, making `pivot` the highest value on the `left`
    - also ensures that the problem size is reduced by at least one for each recursive step

## Visualization

numbers = `[4, 3, 9, 4, 6, 1, 6, 8]` ; k = `3` ; expected = `6`

Where:
- `qs()` is short for `quickselect()`
- `d` is recursive `depth`
- `p` is the `pivot`

```python
d  k  numbers            p  left        right         result
0  3  [4,3,9,4,6,1,6,8]  4  [3,1,4]     [9,4,6,6,8]   recursive at depth 1    
1 -5  [3,1,4]                                         base case: k < 1 ; return None
1  3  [9,4,6,6,8]        9  [4,6,6,8,9] []            recursive at depth 2
2  3  [4,6,6,8,9]        4  [4]         [6,6,8,9]     recursive at depth 3
3 -1  [4]                                             base case: k < 1 ; return None
3  3  [6,6,8,9]          6  [6]         [6,8,9]       recursive at depth 4
4  0  [6]                                             base case: k < 1 ; return None
4  3  [6,8,9]                                         base case: len == k ; return min()

return min(numbers) == 6
```

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest quickselect_1.py`
- `pytest quickselect_2.py`

## Benchmarks

Winners:
- Random: **Zero-Index Pivot - Recursive**
- Sorted: **Half-Index Pivot - Recursive**
- Overall: **Half-Index Pivot - Iterative**

The iterative approach has the added benefit of avoiding recursion limits.

Benched using `timeit` in `benchmarks.py`:
1. Zero-Index Pivot (`numbers[0]`) - Recursive
    - Random: `22.55` seconds
    - Sorted: `47.12` seconds
2. Half-index pivot (`len(numbers) // 2`) - Recursive
    - Random: `34.41` seconds
    - Sorted: `26.18` seconds
3. Half-index pivot (`len(numbers) // 2`) - Iterative
    - Random: `25.83` seconds
    - Sorted: `21.69` seconds
