from collections import defaultdict
from itertools import accumulate, pairwise
from typing import DefaultDict, List


def split_painting(segments: List[List[int]]) -> List[List[int]]:
    painting: DefaultDict[int, int] = defaultdict(int)
    for start, end, color in segments:
        painting[start] += color
        painting[end] -= color
    indexes = sorted(painting)
    colors = accumulate(map(painting.get, indexes))
    return [
        [start, end, color]
        for (start, end), color in zip(pairwise(indexes), colors)
        if color
    ]


def test_example_1():
    assert split_painting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [[1, 4, 14], [4, 7, 16]]


def test_example_2():
    assert split_painting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [
        [1, 6, 9],
        [6, 7, 24],
        [7, 8, 15],
        [8, 10, 7],
    ]


def test_example_3():
    assert split_painting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [
        [1, 4, 12],
        [4, 7, 12],
    ]


def test_odd():
    assert split_painting(
        [
            [4, 16, 12],
            [9, 10, 15],
            [18, 19, 13],
            [3, 13, 20],
            [12, 16, 3],
            [2, 10, 10],
            [3, 11, 4],
            [13, 16, 6],
        ]
    ) == [
        [2, 3, 10],
        [3, 4, 34],
        [4, 9, 46],
        [9, 10, 61],
        [10, 11, 36],
        [11, 12, 32],
        [12, 13, 35],
        [13, 16, 21],
        [18, 19, 13],
    ]
