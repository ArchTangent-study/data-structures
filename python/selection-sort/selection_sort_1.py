# Selection sort algorithm (Version 1)

from typing import List

def find_smallest(values: List) -> int:
    """Returns the *index* of the smallest value in the list. Requires length > 0."""
    smallest = values[0]
    smallest_index = 0

    for i, value in enumerate(values):
        if value < smallest:
            smallest = value
            smallest_index = i

    return smallest_index 


def selection_sort(values: List):
    """Sorts `values` from smallest to largest."""
    output = []

    for _ix in range(len(values)):
        smallest_ix = find_smallest(values)
        output.append(values.pop(smallest_ix))

    return output


def test_selection_sort():
    suite = [
        ([], []),
        ([0], [0]),
        ([1, 0], [0, 1]),
        ([1, 2, 0], [0, 1, 2]),
        ([1, 2, 0, 1], [0, 1, 1, 2]),
        ([-3, -5, 4, 1, -2, 2, 0, -1], [-5, -3, -2, -1, 0, 1, 2, 4]),
    ]
    for input, expected in suite:
        assert selection_sort(input) == expected
