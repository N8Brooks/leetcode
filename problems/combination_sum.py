from collections import Counter, defaultdict
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combo_sums = defaultdict(list)
    for candidate in candidates:
        if candidate > target:
            continue
        # Using a de-normalized tuple instead of a Counter has less overhead
        candidate_count = Counter((candidate,))
        combo_sums[candidate].append(candidate_count)
        for combo_sum in range(candidate, target + 1):
            for counts in combo_sums[combo_sum - candidate]:
                combo_sums[combo_sum].append(counts + candidate_count)
    return [list(counts.elements()) for counts in combo_sums[target]]
