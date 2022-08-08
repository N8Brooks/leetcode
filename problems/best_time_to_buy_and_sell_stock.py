from itertools import accumulate
from operator import sub
from typing import List


def max_profit(prices: List[int]) -> int:
    return max(0, *map(sub, prices, accumulate(prices, min)))
