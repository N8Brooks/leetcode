def calculate(s: str) -> int:
    operand = 0
    result, operator = 0, 1
    stack = []
    for char in s:
        if "0" <= char <= "9":
            operand = 10 * operand + ord(char) - ord("0")
        elif char in ("+", "-"):
            result += operator * operand
            operator = 1 if char == "+" else -1
            operand = 0
        elif char == "(":
            stack.append((result, operator))
            result, operator = 0, 1
        elif char == ")":
            operand = result + operator * operand
            result, operator = stack.pop()
    return result + operator * operand
