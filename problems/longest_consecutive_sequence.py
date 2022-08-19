from itertools import count
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    set_nums = frozenset(nums)
    return max(
        (
            next(j for j in count(i + 1) if j not in set_nums) - i
            for i in set_nums
            if i - 1 not in set_nums
        ),
        default=0,
    )
