from problems.maximum_subarray import max_sub_array


def test_example_1():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example_2():
    assert max_sub_array([1]) == 1


def test_example_3():
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
