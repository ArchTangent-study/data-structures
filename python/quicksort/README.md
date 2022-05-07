# Quicksort

Quicksort implementations in Python, with testing available via `pytest`.  Used to sort values in an array (Python `list`) from lowest to highest.

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
    - *partition* the input at a *pivot*: random index in the array (e.g. index [0])
    - gather values less than pivot in *left partition* (not sorted)
    - gather values greater than pivot in *right partition* (not sorted)
    - return `quicksort(left_partition) + [pivot] + quicksort(right_partition)`
3. Perform above steps recursively until finished.

## Visualization

Length of `input` is `8`.

```
input   3 4 9 4 6 1 6 8

step 1  1                       length > 2, so D&C a     
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
- `pytest quicksort_1.py`
