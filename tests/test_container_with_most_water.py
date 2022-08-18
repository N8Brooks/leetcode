from problems.container_with_most_water import max_area


def test_example_1() -> None:
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2() -> None:
    assert max_area([1, 1]) == 1
