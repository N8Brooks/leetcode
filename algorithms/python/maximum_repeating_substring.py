from itertools import count


def max_repeating(sequence: str, word: str) -> int:
    return next(i - 1 for i in count(1) if word * i not in sequence)


def test_example_1():
    assert max_repeating("ababc", "ab") == 2


def test_example_2():
    assert max_repeating("ababc", "ba") == 1


def test_example_3():
    assert max_repeating("ababc", "ac") == 0
