from itertools import accumulate
from typing import List


def max_sub_array(nums: List[int]) -> int:
    return max(accumulate(nums, lambda x, y: max(x + y, y)))
