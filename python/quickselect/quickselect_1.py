# Quickselect algorithm - Kth Largest (Version 1)
#
# Base cases:
# 1.) k < 1: no answer -> None
# 2.) k == 1: kth largest is the largest of current list
# 3.) Length of list < k: no answer -> None
# 4.) Length of list == k: kth largest is the lowest of current list 
#
# Recursive case:
# 1.) divide and conquer at a random index (the *pivot*)
#   - add pivot to end of LHS
#
# Pitfalls / Caveats:
# 1.) Not enough values to provide `Kth` largest (len(numbers) < k)
# 2.) Duplicate values
# 3.) Python and `falsy` values: need to specify LHS/RHS as `is not None`, because
# if the answer is `0`, it will be considered `false` if you use `if lhs` or `if rhs`.
# 4.) Proper handling of `pivot`: add it to the end of the LHS, making if the highest
# value in the `left` list, and ensuring
from typing import List, Optional

def quickselect(numbers: List, k: int) -> Optional[int]:
    """Finds `Kth` largest value with 0-indexed pivot (recursive)."""
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
    pivot = numbers[0]

    left = []
    right = []
    for n in numbers[1:]:
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

if __name__ == "__main__":
    ans = quickselect([4, 3, 9, 4, 6, 1, 6, 8], 3)

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
