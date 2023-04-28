from problems.longest_palindrome import longest_palindrome


def test_example_1() -> None:
    assert longest_palindrome("abccccdd") == 7


def test_example_2() -> None:
    assert longest_palindrome("a") == 1
