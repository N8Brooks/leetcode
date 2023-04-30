from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) > len(frozenset(nums))


def test_example_1() -> None:
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_example_2() -> None:
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_example_3() -> None:
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
