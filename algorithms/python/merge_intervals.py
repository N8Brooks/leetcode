from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    lo, hi = intervals[0]
    result = []
    for a, b in intervals:
        if a > hi:
            result.append([lo, hi])
            lo = a
            hi = b
        else:
            hi = max(hi, b)
    result.append([lo, hi])
    return result


def test_example_1() -> None:
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_example_2() -> None:
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_cascading() -> None:
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]


def test_backwards() -> None:
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
