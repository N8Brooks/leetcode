from problems.string_to_integer_atoi import my_atoi


def test_example_1():
    assert my_atoi("42") == 42


def test_example_2():
    assert my_atoi("   -42") == -42


def test_example_3():
    assert my_atoi("4193 with words") == 4193


def test_empty():
    assert my_atoi("") == 0


def test_lo():
    assert my_atoi("-91283472332") == -2147483648


def test_hi():
    assert my_atoi("21474836460") == 2147483647
