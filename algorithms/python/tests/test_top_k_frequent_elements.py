from problems.top_k_frequent_elements import top_k_frequent


def test_example_1():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_example_2():
    assert top_k_frequent([1], 1) == [1]
