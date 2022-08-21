from problems.generate_parentheses import generate_parenthesis


def test_example_1():
    assert generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test_example_2():
    assert generate_parenthesis(1) == ["()"]
