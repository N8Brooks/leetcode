from itertools import permutations


def test_example_1():
    actual = list(map(list, permutations([1, 2, 3])))
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert actual == expected


def test_example_2():
    actual = list(map(list, permutations([0, 1])))
    expected = [[0, 1], [1, 0]]
    assert actual == expected


def test_example_3():
    actual = list(map(list, permutations([1])))
    assert actual == [[1]]
