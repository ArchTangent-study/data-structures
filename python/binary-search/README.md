# Binary Search

Binary search implementations in Python, with testing available via `pytest`.

Requirements:
- Integer input, the `target`
- A list with at least one integer value, `numbers`
- Return the list index that contains `target`, if any

Exit Strategy:
- Value is found, *OR*
- Max number of tries remaining is exhausted (`tries_remaining = log2(len(numbers))`) *OR*
- No value present

Edge Cases
- `target` is out of range
- `numbers` has one value
- `numbers` list is empty

Time complexity: O(n) -> linear

## Visualization

Where:
- `L` is the `low_index`
- `M` is the `middle_index`
- `H` is the `high_index`

### Case 1: Value is Present
```
target = 1
numbers = [1,2,3,4,5]

 -1 0 1 2 3 4      Indexes
    L   
        M  
            H
   [1,2,3,4,5]     Step 1: target < numbers[M] -> high index becomes M - 1, recalculate M
     
    L 
    M
      H
   [1,2,3,4,5]     Step 2: target == numbers[M] -> return M
```

### Case 2: Value not Present
```
target = -1
numbers = [1,2,3,4,5]

 -1 0 1 2 3 4      Indexes
    L   
        M  
            H
   [1,2,3,4,5]     Step 1: target < numbers[M] -> high index becomes M - 1, recalculate M

    L 
    M
      H
   [1,2,3,4,5]     Step 2: target < numbers[M] -> high index becomes M - 1, recalculate M

    L   
    M  
    H
   [1,2,3,4,5]     Step 3: target < numbers[M] -> high index becomes M - 1, recalculate M

    L 
    M
  H
   [1,2,3,4,5]     Step 4: EXIT CASE: H < L -> no solution -> Return None 
```

## Testing

Ensure that `pytest` is installed, then run `pytest binary_search_1.py`.
