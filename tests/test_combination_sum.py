from problems.combination_sum import combination_sum


def test_example_1():
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_example_2():
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_example_3():
    assert combination_sum([2], 1) == []


def test_duplicates():
    assert combination_sum([3, 5, 7], 9) == [[3, 3, 3]]


def test_small():
    assert combination_sum([2], 1) == []
