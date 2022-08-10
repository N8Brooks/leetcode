from math import trunc
from typing import List


def eval_rpn(tokens: List[str]) -> int:
    operand = None
    stack = []
    for token in tokens:
        if token == "+":
            operand += stack.pop()
        elif token == "-":
            operand = stack.pop() - operand
        elif token == "*":
            operand *= stack.pop()
        elif token == "/":
            operand = trunc(stack.pop() / operand)
        else:
            if operand is not None:
                stack.append(operand)
            operand = int(token)
    return operand
