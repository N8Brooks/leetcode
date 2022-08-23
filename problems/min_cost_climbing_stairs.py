from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    a = b = 0
    for c in cost:
        a, b = b, min(a, b) + c
    return min(a, b)
