def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        match char:
            case "(":
                stack.append(")")
            case "{":
                stack.append("}")
            case "[":
                stack.append("]")
            case _ if not stack or char != stack.pop():
                return False
    return not stack


def test_example_1() -> None:
    assert is_valid("()") is True


def test_example_2() -> None:
    assert is_valid("()[]{}") is True


def test_example_3() -> None:
    assert is_valid("(]") is False
