from problems.add_binary import add_binary


def test_example_1() -> None:
    assert add_binary("11", "1") == "100"


def test_example_2() -> None:
    assert add_binary("1010", "1011") == "10101"
