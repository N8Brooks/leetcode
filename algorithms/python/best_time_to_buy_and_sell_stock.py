from itertools import accumulate
from operator import sub
from typing import List


def max_profit(prices: List[int]) -> int:
    return max(map(sub, prices, accumulate(prices, min)), default=0)


def test_example_1() -> None:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_example_2() -> None:
    assert max_profit([7, 6, 4, 3, 1]) == 0
