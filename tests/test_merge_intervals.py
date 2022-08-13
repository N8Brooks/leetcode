from problems.merge_intervals import merge


def test_example_1():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_example_2():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_cascading():
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]


def test_backwards():
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
