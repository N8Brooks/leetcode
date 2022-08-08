from problems.valid_palindrome import is_palindrome


def test_example_1():
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_example_2():
    assert is_palindrome("race a car") == False


def test_example_3():
    assert is_palindrome(" ") == True
