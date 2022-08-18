from collections import Counter
from itertools import combinations
from typing import List

# mypy: ignore-errors


def three_sum(nums: List[int]) -> List[List[int]]:
    counts = Counter(nums)
    result = {(0, 0, 0)} if counts[0] >= 3 else set()
    for a, b in combinations(counts, 2):
        c = -a - b
        if counts[c] >= 2 if c in (a, b) else c in counts:
            result.add(tuple(sorted((a, b, c))))
    return result
