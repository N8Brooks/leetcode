from problems.basic_calculator import calculate


def test_example_1():
    assert calculate("1 + 1") == 2


def test_example_2():
    assert calculate("2-1 + 2") == 3


def test_example_3():
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23


def test_inverse():
    assert calculate("- (3 + (4 + 5))") == -12


def test_first():
    assert calculate("(5-(1+(5)))") == -1
