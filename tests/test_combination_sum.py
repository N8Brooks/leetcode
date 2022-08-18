from problems.combination_sum import combination_sum


def test_example_1() -> None:
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_example_2() -> None:
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_example_3() -> None:
    assert combination_sum([2], 1) == []


def test_duplicates() -> None:
    assert combination_sum([3, 5, 7], 9) == [[3, 3, 3]]


def test_small() -> None:
    assert combination_sum([2], 1) == []
