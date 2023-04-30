from itertools import permutations
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    return [list(nums) for nums in permutations(nums)]


# mypy: ignore-errors


def test_example_1() -> None:
    actual = list(map(list, permutations([1, 2, 3])))
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert actual == expected


def test_example_2() -> None:
    actual = list(map(list, permutations([0, 1])))
    expected = [[0, 1], [1, 0]]
    assert actual == expected


def test_example_3() -> None:
    actual = list(map(list, permutations([1])))
    assert actual == [[1]]
