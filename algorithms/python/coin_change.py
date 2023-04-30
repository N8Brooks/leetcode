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


def test_example_1() -> None:
    assert coin_change([1, 2, 5], 11) == 3


def test_example_2() -> None:
    assert coin_change([2], 3) == -1


def test_example_3() -> None:
    assert coin_change([1], 0) == 0


def test_more() -> None:
    assert coin_change([1, 2, 5], 100) == 20


def test_most() -> None:
    assert coin_change([478, 487, 16, 338], 1990) == 15


def test_small() -> None:
    assert coin_change([2], 3) == -1


def test_obscure() -> None:
    assert coin_change([186, 419, 83, 408], 6249) == 20


def test_other() -> None:
    assert coin_change([3, 7, 405, 436], 8839) == 25


def test_larger() -> None:
    assert coin_change([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], 9999) == -1


def test_largest() -> None:
    assert (
        coin_change([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864)
        == 24
    )
