from problems.oranges_rotting import oranges_rotting


def test_example_1() -> None:
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_example_2() -> None:
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_example_3() -> None:
    assert oranges_rotting([[0, 2]]) == 0


def test_zero() -> None:
    assert oranges_rotting([[0]]) == 0


def test_one() -> None:
    assert oranges_rotting([[1]]) == -1


def test_oh_two() -> None:
    assert oranges_rotting([[0, 2]]) == 0
