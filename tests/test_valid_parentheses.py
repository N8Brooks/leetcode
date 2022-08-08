from problems.valid_parentheses import is_valid


def test_example_1():
    assert is_valid("()") == True


def test_example_2():
    assert is_valid("()[]{}") == True


def test_example_3():
    assert is_valid("(]") == False
