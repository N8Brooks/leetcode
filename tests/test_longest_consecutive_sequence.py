from problems.longest_consecutive_sequence import longest_consecutive


def test_example_1():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example_2():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty():
    assert longest_consecutive([]) == 0


def test_zero():
    assert longest_consecutive([0]) == 1
