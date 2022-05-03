# Selection Sort

Selection sort implementations in Python, with testing available via `pytest`.  Used to sort values in an array (Python `list`) from lowest to highest.

Requirements:
- Input is an array
- Values in the array are sortable:  allow the `<` comparison operator

Exit Strategy:
- All values in array have been traversed (had `find_smallest()` applied)

Edge Cases / Caveats:
- Empty array input
- Duplicate (equal) values
- Negative values

Time complexity: `O(n^2)`

## Approach

The overall steps:
1. Create a new array to hold the output
2. For each value in the input (e.g. if five values in array, perform five times):
    - find the smallest value in the input
    - add the smallest value to the output array by:
        - removing it from input first, *OR*
        - simply copying it to input
3. Return the output

## Visualization

Length of `input` is `8`, so there are 8 steps to complete `output`:

```
input   3 4 9 4 6 1 6 8

step 1  1
step 2  1 3
step 3  1 3 4
step 4  1 3 4 4
step 5  1 3 4 4 6
step 6  1 3 4 4 6 6
step 7  1 3 4 4 6 6 8

output  1 3 4 4 6 6 8 9
```

## Testing

Ensure that `pytest` is installed, then run one of the following:
- `pytest selection_sort_1.py`
