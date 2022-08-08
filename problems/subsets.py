from itertools import combinations, chain
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    return chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
