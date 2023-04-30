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


def test_example_1() -> None:
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_example_2() -> None:
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_example_3() -> None:
    assert combination_sum([2], 1) == []


def test_duplicates() -> None:
    assert combination_sum([3, 5, 7], 9) == [[3, 3, 3]]


def test_small() -> None:
    assert combination_sum([2], 1) == []
