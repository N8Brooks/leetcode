from collections import Counter
from itertools import combinations
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    counts = Counter(nums)
    result = {(0, 0, 0)} if counts[0] >= 3 else set()
    for a, b in combinations(counts, 2):
        c = -a - b
        if counts[c] >= 2 if c in (a, b) else c in counts:
            result.add(tuple(sorted((a, b, c))))  # type: ignore
    return [list(abc) for abc in result]


# mypy: ignore-errors


def test_example_1() -> None:
    assert sorted(map(list, three_sum([-1, 0, 1, 2, -1, -4]))) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_example_2() -> None:
    assert sorted(map(list, three_sum([0, 1, 1]))) == []


def test_example_3() -> None:
    assert sorted(map(list, three_sum([0, 0, 0]))) == [[0, 0, 0]]
