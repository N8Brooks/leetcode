from problems.minimum_height_trees import find_min_height_trees


def test_example_1() -> None:
    assert find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]) == [1]


def test_example_2() -> None:
    assert find_min_height_trees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4]


def test_empty() -> None:
    assert find_min_height_trees(1, []) == [0]
