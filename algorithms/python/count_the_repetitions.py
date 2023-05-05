from typing import Any, List


def get_max_repetitions(s_1: str, n_1: int, s_2: str, n_2: int) -> int:
    i = 0
    l_2 = len(s_2)
    memo: List[Any] = [None] * l_2

    while n_1:
        for char in s_1:
            if char == s_2[i % l_2]:
                i += 1

        if memo[i % l_2] is None:
            memo[i % l_2] = (n_1, i)
        else:
            pre_n1, pre_i = memo[i % l_2]
            count = (n_1 - 1) // (pre_n1 - n_1)
            i += (i - pre_i) * count
            n_1 -= (pre_n1 - n_1) * count

        n_1 -= 1

    return i // l_2 // n_2


def test_example_1():
    assert get_max_repetitions(s_1="acb", n_1=4, s_2="ab", n_2=2) == 2


def test_example_2():
    assert get_max_repetitions(s_1="acb", n_1=1, s_2="acb", n_2=1) == 1


def test_baba():
    assert (
        get_max_repetitions(
            "baba",
            11,
            "baab",
            1,
        )
        == 7
    )
