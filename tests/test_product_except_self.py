from problems.product_except_self import product_except_self


def test_example_1() -> None:
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example_2() -> None:
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_zeros() -> None:
    assert product_except_self([0, 0]) == [0, 0]
