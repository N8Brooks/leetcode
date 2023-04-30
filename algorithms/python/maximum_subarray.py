from itertools import accumulate
from typing import List


def max_sub_array(nums: List[int]) -> int:
    return max(accumulate(nums, lambda x, y: max(x + y, y)))


def test_example_1() -> None:
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example_2() -> None:
    assert max_sub_array([1]) == 1


def test_example_3() -> None:
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
