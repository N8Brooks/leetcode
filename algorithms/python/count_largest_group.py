from collections import Counter
from itertools import groupby


def count_largest_group(n: int) -> int:
    counts = Counter(sum(map(int, f"{i}")) for i in range(1, n + 1))
    largest_groups = next(groupby(count for _, count in counts.most_common()))
    return len(tuple(largest_groups[1]))


def test_example_1():
    assert count_largest_group(13) == 4


def test_example_2():
    assert count_largest_group(2) == 2
