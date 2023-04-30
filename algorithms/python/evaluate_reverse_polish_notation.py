from math import trunc
from typing import List


def eval_rpn(tokens: List[str]) -> int:
    operand = 0
    stack: List[int] = []
    for token in tokens:
        match token:
            case "+":
                operand += stack.pop()
            case "-":
                operand = stack.pop() - operand
            case "*":
                operand *= stack.pop()
            case "/":
                operand = trunc(stack.pop() / operand)
            case _:
                if operand is not None:
                    stack.append(operand)
                operand = int(token)
    return operand


def test_example_1() -> None:
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_example_2() -> None:
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_example_3() -> None:
    assert (
        eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )


def test_minus() -> None:
    assert eval_rpn(["4", "3", "-"]) == 1
