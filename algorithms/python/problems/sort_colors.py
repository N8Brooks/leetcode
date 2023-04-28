from itertools import repeat
from typing import List


def sort_colors(nums: List[int]) -> None:
    """Bucket sort for values 0, 1, and 2"""
    i = nums.count(0)
    j = len(nums) - nums.count(2)
    nums[:i] = repeat(0, i)
    nums[i:j] = repeat(1, j - i)
    nums[j:] = repeat(2, len(nums) - j)
