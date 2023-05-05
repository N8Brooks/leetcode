from collections import Counter
from itertools import accumulate
from typing import List


def min_set_size(arr: List[int]) -> int:
    removed = accumulate(count for _, count in Counter(arr).most_common())
    return next(i + 1 for i, x in enumerate(removed) if x >= len(arr) / 2)


def test_example_1():
    assert min_set_size([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2


def test_example_2():
    assert min_set_size([7, 7, 7, 7, 7, 7]) == 1
