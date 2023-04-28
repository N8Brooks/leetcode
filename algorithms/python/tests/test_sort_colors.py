from problems.sort_colors import sort_colors


def test_example_1() -> None:
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_example_2() -> None:
    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2]
