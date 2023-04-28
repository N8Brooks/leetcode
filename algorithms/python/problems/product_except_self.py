from itertools import accumulate
from operator import mul
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    lprod = accumulate(nums, mul, initial=1)
    rprod = tuple(accumulate(reversed(nums), mul, initial=1))[-2::-1]
    return list(map(mul, lprod, rprod))
