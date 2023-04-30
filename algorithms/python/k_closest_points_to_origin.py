from heapq import nsmallest
from math import hypot
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    return nsmallest(k, points, key=lambda p: hypot(*p))


def test_example_1() -> None:
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_example_2() -> None:
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
