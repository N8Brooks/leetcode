from itertools import chain, pairwise
from typing import List


def large_group_positions(s: str) -> List[List[int]]:
    return [
        [a, b - 1]
        for a, b in pairwise(
            i for i, (a, b) in enumerate(pairwise(chain("$", s, "^"))) if a != b
        )
        if b - a > 2
    ]


def test_example_1():
    assert large_group_positions("abbxxxxzzy") == [[3, 6]]


def test_example_2():
    assert large_group_positions("abc") == []


def test_example_3():
    assert large_group_positions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]
