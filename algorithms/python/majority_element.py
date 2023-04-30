from statistics import mode
from typing import List


def majority_element(nums: List[int]) -> int:
    return mode(nums)


def test_example_1() -> None:
    assert majority_element([3, 2, 3]) == 3


def test_example_2() -> None:
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
