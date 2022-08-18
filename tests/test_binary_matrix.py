from problems.binary_matrix import update_matrix


def test_example_1() -> None:
    actual = update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert actual == expected


def test_example_2() -> None:
    actual = update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert actual == expected


def test_small() -> None:
    actual = update_matrix([[0], [1]])
    expected = [[0], [1]]
    assert actual == expected
