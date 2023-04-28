from problems.valid_parentheses import is_valid


def test_example_1() -> None:
    assert is_valid("()") is True


def test_example_2() -> None:
    assert is_valid("()[]{}") is True


def test_example_3() -> None:
    assert is_valid("(]") is False
