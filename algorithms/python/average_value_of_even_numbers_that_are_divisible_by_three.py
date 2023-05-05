from typing import List


def average_value(nums: List[int]) -> int:
    nums = [num for num in nums if num % 6 == 0]
    return sum(nums) // len(nums) if nums else 0


def test_example_1():
    assert average_value([1, 3, 6, 10, 12, 15]) == 9


def test_example_2():
    assert average_value([1, 2, 4, 7, 10]) == 0


def test_9():
    assert average_value([4, 4, 9, 10]) == 0
