# Binary Search in Python - Version 1: Tries Remaining

from typing import Optional, List
from math import log2

def binary_search(target: int, numbers: List[int]) -> Optional[int]:
    """Returns the index of `target` in `numbers`, if present."""
    length = len(numbers)
    if length == 0 or target < numbers[0] or target > numbers[-1]:
        return None

    low_ix = 0
    high_ix = length - 1
    tries_remaining = int(log2(length)) + 1
    
    while tries_remaining > 0:
        current_ix = (low_ix + high_ix) // 2
        number = numbers[current_ix]

        if target == number:
            return current_ix
        elif target < number:
            high_ix = current_ix - 1
        else:
            low_ix = current_ix + 1

        tries_remaining -= 1

    return None


def test_binary_search():
    battery = [
        [1, [], None],
        [4, [1, 2, 3, 5], None],
        [3, [1, 2, 4], None],
        [-1, [1, 2, 3, 4, 5], None],
        [6, [1, 2, 3, 4, 5], None],
        [1, [1], 0],
        [1, [1, 2, 3, 4, 5], 0],
        [2, [1, 2, 3, 4, 5], 1],
        [3, [1, 2, 3, 4, 5], 2],
        [4, [1, 2, 3, 4, 5], 3],
        [5, [1, 2, 3, 4, 5], 4],
    ]

    for target, numbers, answer in battery:
        assert binary_search(target, numbers) == answer

