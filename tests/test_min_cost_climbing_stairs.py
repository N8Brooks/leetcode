from problems.min_cost_climbing_stairs import min_cost_climbing_stairs


def test_example_1():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15


def test_example_2():
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
