from problems.unique_paths import unique_paths


def test_example_1() -> None:
    assert unique_paths(3, 7) == 28


def test_example_2() -> None:
    assert unique_paths(3, 2) == 3


def test_moderate() -> None:
    assert unique_paths(4, 6) == 56


def test_square() -> None:
    assert unique_paths(4, 4) == 20


def test_two_by_two() -> None:
    assert unique_paths(2, 2) == 2
