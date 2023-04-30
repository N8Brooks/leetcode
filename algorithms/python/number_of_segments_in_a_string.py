from itertools import groupby


def count_segments(s: str) -> int:
    return sum(c for c, _ in groupby(s, lambda c: c != " "))


def test_example_1():
    assert count_segments("Hello, my name is John") == 5


def test_example_2():
    assert count_segments("Hello") == 1


def test_blank():
    assert count_segments("") == 0


def test_non_words():
    assert count_segments("love live! mu'sic forever") == 4
