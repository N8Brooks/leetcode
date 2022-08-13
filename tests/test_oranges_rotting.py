from problems.oranges_rotting import oranges_rotting


def test_example_1():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_example_2():
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_example_3():
    assert oranges_rotting([[0, 2]]) == 0


def test_zero():
    assert oranges_rotting([[0]]) == 0


def test_one():
    assert oranges_rotting([[1]]) == -1


def test_oh_two():
    assert oranges_rotting([[0, 2]]) == 0
