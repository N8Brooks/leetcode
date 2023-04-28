from problems.longest_increasing_subsequence import length_of_lis


def test_example_1():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example_2():
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4


def test_example_3():
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1


def test_negative():
    assert length_of_lis([-2, -1]) == 2
