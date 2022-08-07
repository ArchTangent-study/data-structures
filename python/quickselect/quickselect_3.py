# Quickselect algorithm - Kth Largest (Version 3)
# 
# Key Characteristics:
# 1.) non-recursive
# 2.) pivot is cental: length(numbers) // 2
# 3.) raises an error if input is invalid (invalid k, empty numbers)
#
# Don't need recursion as only one of two branches is ever valid. Can simply replace
# the `numbers` list with its new values each time until answer or None is found.
from typing import List

def quickselect(numbers: List, k: int) -> int:
    """Finds `Kth` largest value with half-length pivot (iterative)."""
    length = len(numbers)

    # Invalid data
    if length == 0:
        raise ValueError("no numbers provided!")
    if k < 0 or k > length:
        raise ValueError("Must have 0 < k <= len(numbers)!")

    # Copy numbers to avoid side effects
    nums = numbers[:]

    # Can loop forever since answer will be present
    while True:
        length = len(nums)
                
        # Base Cases: find largest or smallest number in list
        if k == 1:
            return max(nums)
        if k == length:
            return min(nums)

        # Iterative case: pivot and choose either left or right side
        # NOTE: pivot is added to the LHS, after everything less than it
        pivot_ix = length // 2
        pivot = nums[length // 2]

        left = []
        right = []

        for n in nums[:pivot_ix]:
            if n < pivot:
                left.append(n)
            else:
                right.append(n)
        for n in nums[pivot_ix+1:]:
            if n < pivot:
                left.append(n)
            else:
                right.append(n)

        # Choose left or right path: only one is valid
        if len(right) >= k:
            # Right side
            nums = right
        else:
            # Left side
            # NOTE: pivot appended here, since only relevant if left side is chosen
            left.append(pivot)
            k_left = k - len(right)
            k = k_left
            nums = left


def test_quickselect():
    import pytest

    suite = [
        ([1,2,3,4], 1, 4),
        ([1,2,3,4], 2, 3),
        ([1,2,3,4], 3, 2),
        ([1,2,3,4], 4, 1),
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

    suite_fail = [
        ([1,2,3,4], 5),
        ([], 5),
        ([1,2,3,4], 0),
    ]

    for input, k,  expected in suite:
        assert quickselect(input, k) == expected

    for input, k in suite_fail:
        with pytest.raises(ValueError) as exc_info:
            quickselect(input, k)
            assert exc_info.type is ValueError
