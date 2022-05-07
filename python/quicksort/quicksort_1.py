# Quicksort algorithm (Version 1)
#
# Three base cases:
# 1.) Empty list -> empty list []
# 2.) One item -> one item [n]
# 3.) Two items -> two items in order [m, n]
# Otherwise, recursively divide and conquer at a random index (the *pivot*)
#
# Pitfalls:
# 1.) Indexing: make sure *not* to include the pivot when creating `left` and `right` lists

from typing import List


def quicksort(values: List) -> List:
    """Sorts `values` from smallest to largest."""
    length = len(values)

    match length:
        case 0 | 1:
            return values
        case 2:
            if values[0] < values[1]:
                return [values[0], values[1]]
            else:
                return [values[1], values[0]]
        case _:
            pivot = values[0]
            left = [v for v in values[1:] if v <= pivot]
            right = [v for v in values[1:] if v > pivot]

            return quicksort(left) + [pivot] + quicksort(right)


def test_quicksort():
    suite = [
        ([], []),
        ([0], [0]),
        ([1, 0], [0, 1]),
        ([1, 2, 0], [0, 1, 2]),
        ([1, 2, 0, 1], [0, 1, 1, 2]),
        ([-1, -2, 0, -1, -2], [-2, -2, -1, -1, 0]),
        ([-3, -5, 4, 1, -2, 2, 0, -1], [-5, -3, -2, -1, 0, 1, 2, 4]),
    ]
    for input, expected in suite:
        assert quicksort(input) == expected
