from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    indices: Dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return [indices[complement], i]
        indices[num] = i
    raise ValueError("no two sum")
