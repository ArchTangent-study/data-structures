# Quicksort

[Quicksort](https://en.wikipedia.org/wiki/Quicksort) implementations in Python, with testing available via `pytest`.  Used to sort values in an array (Python `list`) from lowest to highest.

Requirements:
- Input is an array
- Values in the array are sortable:  allow the `<` comparison operator

Edge Cases / Caveats:
- Empty array input
- Duplicate (equal) values
- Negative values

Time complexity: `O(n log n)` average case

## Approach

Use a divide and conquer (D&C) strategy to break the problem down into reusable, recursive steps.

The process:
1. Check *base case*: length of input < `2`:
    - return the input (no need to sort)
2. Check *recursive case*: length of input >= `2`:
    - *partition* the input at a `pivot`: random index in the array (e.g. index [0])
    - gather values less than pivot in `left_partition` (not sorted)
    - gather values greater than pivot in `right_partition` (not sorted)
    - return `quicksort(left_partition) + [pivot] + quicksort(right_partition)`
3. Perform above steps recursively until finished.

## Visualization

Input: `[4, 3, 9, 4, 6, 1, 6, 8]`

Length of `input`: `8`

Where: `qs()` is short for `quicksort()`

```python
start   [4, 3, 9, 4, 6, 1, 6, 8]

step_1  qs([3,4,1]) + [4] + qs([9,6,6,8])
step_2  qs([1]) + [3] + qs([4]) + [4] + qs([6,6,8]) + [9] + qs([])
step_3  [1] + [3] + [4] + [4] + qs([6]) + [6] + qs([8]) + [9] + []
step_4  [1] + [3] + [4] + [4] + [6] + [6] + [8] + [9] + []  

finish  [1, 3, 4, 4, 6, 6, 8, 9]
```

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest quicksort_1.py` OR
- `pytest quicksort_2.py`
