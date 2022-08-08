from collections import deque


def is_palindrome(s: str) -> bool:
    s = deque(filter(str.isalnum, s.lower()))
    while len(s) > 1:
        if s.popleft() != s.pop():
            return False
    return True
