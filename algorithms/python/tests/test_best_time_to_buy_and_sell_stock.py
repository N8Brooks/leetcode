from problems.best_time_to_buy_and_sell_stock import max_profit


def test_example_1() -> None:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_example_2() -> None:
    assert max_profit([7, 6, 4, 3, 1]) == 0
