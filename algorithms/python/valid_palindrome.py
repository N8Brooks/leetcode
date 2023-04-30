def is_palindrome(s: str) -> bool:
    s = "".join(filter(str.isalnum, s.lower()))
    return s == s[::-1]


def test_example_1() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_example_2() -> None:
    assert is_palindrome("race a car") is False


def test_example_3() -> None:
    assert is_palindrome(" ") is True
