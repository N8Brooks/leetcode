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
