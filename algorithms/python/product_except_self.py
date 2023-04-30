from itertools import accumulate
from operator import mul
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    lprod = accumulate(nums, mul, initial=1)
    rprod = tuple(accumulate(reversed(nums), mul, initial=1))[-2::-1]
    return list(map(mul, lprod, rprod))


def test_example_1() -> None:
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2() -> None:
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_zeros() -> None:
    assert product_except_self([0, 0]) == [0, 0]
