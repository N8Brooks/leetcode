from problems.longest_palindromic_substring import longest_palindrome


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
