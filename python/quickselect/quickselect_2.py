# Quickselect algorithm - Kth Largest (Version 2)
# 
# Differences from V1:
# 1.) pivot will be central: length(numbers) // 2
from typing import List, Optional

def quickselect(numbers: List, k: int) -> Optional[int]:
    """Finds `Kth` largest value with half-length pivot (recursive)."""
    length = len(numbers)

    # Base Cases
    if k < 1:
        return None
    if k == 1:
        return max(numbers)
    if length < k:
        return None
    if length == k:
        return min(numbers)
    
    # Recursive case
    # NOTE: pivot is added to the LHS, after everything less than it
    pivot_ix = length // 2
    pivot = numbers[length // 2]

    left = []
    right = []
    for ix, n in enumerate(numbers):
        if ix == pivot_ix:
            continue
        if n < pivot:
            left.append(n)
        else:
            right.append(n)

    left.append(pivot)

    # For left side, k becomes `k - len(right)`
    lhs =  quickselect(left, k - len(right))
    rhs =  quickselect(right, k)

    # Only one correct answer, if any
    if lhs is not None:
        return lhs
    if rhs is not None:
        return rhs
    
    return None

def test_quickselect():
    suite = [
        ([], 5, None),
        ([1,2,3,4], 0, None),
        ([1,2,3,4], 1, 4),
        ([1,2,3,4], 2, 3),
        ([1,2,3,4], 3, 2),
        ([1,2,3,4], 4, 1),
        ([1,2,3,4], 5, None),
        ([4,1,2,3], 1, 4),
        ([4,1,2,3], 2, 3),
        ([4,1,2,3], 3, 2),
        ([4,1,2,3], 4, 1),
        ([3,4,1,2], 1, 4),
        ([3,4,1,2], 2, 3),
        ([3,4,1,2], 3, 2),
        ([3,4,1,2], 4, 1),
        ([2,3,4,1], 1, 4),
        ([2,3,4,1], 2, 3),
        ([2,3,4,1], 3, 2),
        ([2,3,4,1], 4, 1),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 1, 4),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 5, 3),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 8, 2),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 10, 1),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 11, 0),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 12, -1),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 13, -2),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 15, -3),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 18, -4),
        ([4,4,4,4,3,3,3,2,2,1,0,-1,-2,-2,-3,-3,-3,-4,-4,-4,-4], 20, -4),
        ([*range(100)], 50, 50)
    ]
    for input, k,  expected in suite:
        assert quickselect(input, k) == expected
