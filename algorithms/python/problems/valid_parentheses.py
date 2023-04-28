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
