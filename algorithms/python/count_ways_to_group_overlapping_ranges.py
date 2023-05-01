from typing import List


def count_ways(ranges: List[List[int]]) -> int:
    ranges.sort()
    count = 0
    cursor = -1
    for start, stop in ranges:
        if start > cursor:
            count += 1
        if stop > cursor:
            cursor = stop
    return pow(2, count, 1_000_000_007)


def test_example_1():
    assert count_ways([[6, 10], [5, 15]]) == 2


def test_example_2():
    assert count_ways([[1, 3], [10, 20], [2, 5], [4, 8]]) == 4


def test_merge():
    assert count_ways([[0, 2], [2, 3]]) == 2


def test_multi_merge():
    assert (
        count_ways([[5, 12], [16, 28], [32, 41], [7, 15], [17, 26], [41, 46], [1, 12]])
        == 8
    )
