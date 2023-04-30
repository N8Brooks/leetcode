from typing import List


def trap(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    left_max = right_max = 0
    water = 0
    while i <= j:
        if left_max < right_max:
            left_max = max(left_max, height[i])
            water += left_max - height[i]
            i += 1
        else:
            right_max = max(right_max, height[j])
            water += right_max - height[j]
            j -= 1
    return water


def test_example_1() -> None:
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_example_2() -> None:
    assert trap([4, 2, 0, 3, 2, 5]) == 9


def test_empty() -> None:
    assert trap([]) == 0


def test_mountain() -> None:
    assert trap([0, 2, 0]) == 0
