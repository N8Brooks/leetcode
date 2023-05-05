from typing import Dict, List


def merge_arrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    nums: Dict[int, int] = dict(nums1)  # type: ignore
    for key, val in nums2:
        nums[key] = nums.get(key, 0) + val
    return [[key, nums[key]] for key in sorted(nums)]


def test_example_1():
    assert merge_arrays(
        nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]
    ) == [[1, 6], [2, 3], [3, 2], [4, 6]]


def test_example_2():
    assert merge_arrays(nums1=[[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]]) == [
        [1, 3],
        [2, 4],
        [3, 6],
        [4, 3],
        [5, 5],
    ]
