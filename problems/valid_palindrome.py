def is_palindrome(s: str) -> bool:
    s = "".join(filter(str.isalnum, s.lower()))
    return all(s[i] == s[-1 - i] for i in range(len(s) // 2))
