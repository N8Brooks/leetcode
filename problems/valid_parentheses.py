def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char == "(":
            stack.append(")")
        elif char == "{":
            stack.append("}")
        elif char == "[":
            stack.append("]")
        elif not stack:
            return False
        elif char != stack.pop():
            return False
    return not stack
