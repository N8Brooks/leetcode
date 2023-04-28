from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    to_collect = 1 << amount
    n = 0
    while not to_collect & 1:
        collected = to_collect
        for coin in coins:
            collected |= to_collect >> coin
        if collected == to_collect:
            return -1
        to_collect ^= collected
        n += 1
    return n
