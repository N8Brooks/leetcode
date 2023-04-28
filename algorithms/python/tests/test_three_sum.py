from problems.three_sum import three_sum

# mypy: ignore-errors


def test_example_1() -> None:
    assert sorted(map(list, three_sum([-1, 0, 1, 2, -1, -4]))) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_example_2() -> None:
    assert sorted(map(list, three_sum([0, 1, 1]))) == []


def test_example_3() -> None:
    assert sorted(map(list, three_sum([0, 0, 0]))) == [[0, 0, 0]]
