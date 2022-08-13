from problems.search_in_rotated_sorted_array import search


def test_example_1():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example_2():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_example_3():
    assert search([1], 0) == -1


def test_five_one_three():
    assert search([5, 1, 3], 5) == 0
