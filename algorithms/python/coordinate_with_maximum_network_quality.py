from itertools import product
from math import dist
from typing import List


def best_coordinate(towers: List[List[int]], radius: int) -> List[int]:
    return list(
        max(
            product(
                range(max(x for x, _, _ in towers) + 1),
                range(max(y for _, y, _ in towers) + 1),
            ),
            key=lambda c: sum(
                q // (1 + d) for *p, q in towers if radius >= (d := dist(c, p))
            ),
        )
    )


def test_example_1():
    assert best_coordinate([[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2) == [2, 1]


def test_example_2():
    assert best_coordinate([[23, 11, 21]], 9) == [23, 11]


def test_example_3():
    assert best_coordinate([[1, 2, 13], [2, 1, 7], [0, 1, 9]], 2) == [1, 2]
