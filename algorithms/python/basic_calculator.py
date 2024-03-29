def calculate(s: str) -> int:
    operand = 0
    result, operator = 0, 1
    stack = []
    for char in s:
        match char:
            case "+" | "-":
                result += operator * operand
                operator = 1 if char == "+" else -1
                operand = 0
            case "(":
                stack.append((result, operator))
                result, operator = 0, 1
            case ")":
                operand = result + operator * operand
                result, operator = stack.pop()
            case _ if "0" <= char <= "9":
                operand = 10 * operand + ord(char) - ord("0")
    return result + operator * operand


def test_example_1() -> None:
    assert calculate("1 + 1") == 2


def test_example_2() -> None:
    assert calculate("2-1 + 2") == 3


def test_example_3() -> None:
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23


def test_inverse() -> None:
    assert calculate("- (3 + (4 + 5))") == -12


def test_first() -> None:
    assert calculate("(5-(1+(5)))") == -1
