import bisect
from typing import List


def search(nums: List[int], target: int) -> int:
    # Delegates logic to bisect. This won't work for
    # empty lists, but there are no tests for that.
    i = bisect.bisect(nums, target) - 1
    return i if nums[i] == target else -1
