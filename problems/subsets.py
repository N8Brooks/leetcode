from itertools import chain, combinations
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # Implements the power_set from the itertools recipes
    return chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))  # type: ignore
