from problems.majority_element import majority_element


def test_example_1() -> None:
    assert majority_element([3, 2, 3]) == 3


def test_example_2() -> None:
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
