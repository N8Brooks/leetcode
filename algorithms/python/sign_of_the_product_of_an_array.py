from math import prod
from typing import List


def array_sign(nums: List[int]) -> int:
    return sign(prod(nums))


def sign(n: int) -> int:
    return (n > 0) - (n < 0)


def test_example_1():
    assert array_sign([-1, -2, -3, -4, 3, 2, 1]) == 1


def test_example_2():
    assert array_sign([1, 5, 0, 2, -3]) == 0


def test_example_3():
    assert array_sign([-1, 1, -1, 1, -1]) == -1
