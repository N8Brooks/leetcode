import bisect
from typing import List


def search(nums: List[int], target: int) -> int:
    i = bisect.bisect(nums, target) - 1
    return i if nums and nums[i] == target else -1
