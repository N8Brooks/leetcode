def replace_digits(s: str) -> str:
    shifted = "".join(c + shift(c, int(x)) for c, x in zip(s[::2], s[1::2]))
    return shifted + s[len(s) - len(s) % 2 :]


def shift(c: str, x: int) -> str:
    return chr(ord(c) + x)


def test_example_1():
    assert replace_digits("a1c1e1") == "abcdef"


def test_example_2():
    assert replace_digits("a1b2c3d4e") == "abbdcfdhe"
