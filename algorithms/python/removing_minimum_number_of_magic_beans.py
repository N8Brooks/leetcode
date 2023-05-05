from operator import mul
from typing import List


def minimum_removal(beans: List[int]) -> int:
    return sum(beans) - max(map(mul, sorted(beans), range(len(beans), 0, -1)))


def test_example_1():
    assert minimum_removal([4, 1, 6, 5]) == 4


def test_example_2():
    assert minimum_removal([2, 10, 3, 2]) == 7
