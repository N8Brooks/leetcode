from problems.two_sum_ii import two_sum


def test_example_1():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]


def test_example_2():
    assert two_sum([2, 3, 4], 6) == [1, 3]


def test_example_3():
    assert two_sum([-1, 0], -1) == [1, 2]
