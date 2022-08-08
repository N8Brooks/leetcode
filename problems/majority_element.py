from statistics import mode
from typing import List


def majority_element(nums: List[int]) -> int:
    return mode(nums)
