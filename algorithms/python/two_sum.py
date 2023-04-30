from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    indices: Dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return [indices[complement], i]
        indices[num] = i
    raise ValueError("no two sum")


def test_example_1() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2() -> None:
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_example_3() -> None:
    assert two_sum([3, 3], 6) == [0, 1]
