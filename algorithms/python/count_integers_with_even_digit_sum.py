def count_even(num: int) -> int:
    return (num - sum(map(int, f"{num}")) % 2) // 2


def test_example_1():
    assert count_even(4) == 2


def test_example_2():
    assert count_even(30) == 14


def test_13():
    assert count_even(13) == 6
