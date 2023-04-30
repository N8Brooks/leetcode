def longest_palindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    i = 1
    length = 1
    for j in range(1, len(s)):
        odd = s[j - length - 1 : j + 1]
        even = s[j - length : j + 1]
        if j - length - 1 >= 0 and odd == odd[::-1]:
            i = j - length - 1
            length += 2
        elif j - length >= 0 and even == even[::-1]:
            i = j - length
            length += 1
    return s[i : i + length]


def test_example_1() -> None:
    assert longest_palindrome("babad") == "bab"


def test_example_2() -> None:
    assert longest_palindrome("cbbd") == "bb"


def test_a() -> None:
    assert longest_palindrome("a") == "a"


def test_last() -> None:
    assert longest_palindrome("abb") == "bb"


def test_empty() -> None:
    assert longest_palindrome("") == ""
