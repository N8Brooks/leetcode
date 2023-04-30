from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test_example_1() -> None:
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example_2() -> None:
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_example_3() -> None:
    assert search([1], 0) == -1


def test_five_one_three() -> None:
    assert search([5, 1, 3], 5) == 0
