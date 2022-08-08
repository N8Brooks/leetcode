from problems.three_sum import three_sum


def test_example_1():
    assert sorted(map(list, three_sum([-1, 0, 1, 2, -1, -4]))) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_example_2():
    assert sorted(map(list, three_sum([0, 1, 1]))) == []


def test_example_3():
    assert sorted(map(list, three_sum([0, 0, 0]))) == [[0, 0, 0]]
