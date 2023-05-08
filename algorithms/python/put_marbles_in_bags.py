from heapq import nlargest, nsmallest
from itertools import pairwise, starmap
from operator import add
from typing import List


def put_marbles(weights: List[int], k: int) -> int:
    maximum = sum(nlargest(k - 1, starmap(add, pairwise(weights))))
    minimum = sum(nsmallest(k - 1, starmap(add, pairwise(weights))))
    return maximum - minimum


def test_example_1():
    assert put_marbles([1, 3, 5, 1], 2) == 4


def test_example_2():
    assert put_marbles([1, 3], 2) == 0


def test_no_split():
    assert put_marbles([25, 74, 16, 51, 12, 48, 15, 5], 1) == 0
