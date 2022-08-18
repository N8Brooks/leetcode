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
