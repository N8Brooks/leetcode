def add_binary(a: str, b: str) -> str:
    return f"{int(a, 2) + int(b, 2):b}"


def test_example_1() -> None:
    assert add_binary("11", "1") == "100"


def test_example_2() -> None:
    assert add_binary("1010", "1011") == "10101"
