from collections import defaultdict
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combo_sums = defaultdict(list)
    for candidate in candidates:
        if candidate > target:
            continue
        combo_sums[candidate].append([candidate])
        for i in range(candidate, target + 1):
            for x in combo_sums[i - candidate]:
                combo_sums[i].append(x + [candidate])
    return combo_sums[target]
