from functools import reduce


# pylint: disable=inconsistent-return-statements
def decode_at_index(s: str, k: int) -> str:
    n = reduce(lambda n, char: n * int(char) if char.isdigit() else n + 1, s, 0)
    for char in reversed(s):
        if char.isdigit():
            n //= int(char)
            k %= n
        elif 0 < k < n:
            n -= 1
        else:
            return char
    raise Exception("invalid input")  # pylint: disable=broad-exception-raised


def test_example_1():
    assert decode_at_index("leet2code3", 10) == "o"


def test_example_2():
    assert decode_at_index("ha22", 5) == "h"


def test_example_3():
    assert decode_at_index("a2345678999999999999999", 1) == "a"


def test_no_repeat():
    assert decode_at_index("abc", 1) == "a"


def test_repeated_repeat():
    assert decode_at_index("a2b3c4d5e6f7g8h9", 9) == "b"
