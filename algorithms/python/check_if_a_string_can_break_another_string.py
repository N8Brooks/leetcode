from itertools import accumulate
from operator import sub
from string import ascii_lowercase


def check_if_can_break(s_1: str, s_2: str) -> bool:
    return can_break(s_1, s_2) or can_break(  # pylint: disable=arguments-out-of-order
        s_2, s_1
    )


def can_break(s_1: str, s_2: str) -> bool:
    return all(
        n >= 0
        for n in accumulate(
            map(
                sub,
                map(s_1.count, ascii_lowercase),
                map(s_2.count, ascii_lowercase),
            )
        )
    )


def test_example_1():
    assert check_if_can_break("abc", "xya")


def test_example_2():
    assert not check_if_can_break("abe", "acd")


def test_example_3():
    assert check_if_can_break("leetcodee", "interview")
