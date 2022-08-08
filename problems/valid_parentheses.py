BRACES = {
    "(": ")",
    "{": "}",
    "[": "]",
}


def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char in BRACES:
            stack.append(BRACES[char])
        elif not stack:
            return False
        elif char != stack.pop():
            return False
    return not stack
