from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    a = b = 0
    for c in cost:
        a, b = b, min(a, b) + c
    return min(a, b)


def test_example_1():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15


def test_example_2():
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
