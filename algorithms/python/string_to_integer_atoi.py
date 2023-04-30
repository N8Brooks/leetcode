import re

PATTERN = re.compile(r"\s*([-+]?\d+)")


def my_atoi(s: str) -> int:
    match = PATTERN.match(s)
    return max(-(2**31), min(2**31 - 1, int(match[0]))) if match else 0


def test_example_1() -> None:
    assert my_atoi("42") == 42


def test_example_2() -> None:
    assert my_atoi("   -42") == -42


def test_example_3() -> None:
    assert my_atoi("4193 with words") == 4193


def test_empty() -> None:
    assert my_atoi("") == 0


def test_lo() -> None:
    assert my_atoi("-91283472332") == -2147483648


def test_hi() -> None:
    assert my_atoi("21474836460") == 2147483647
