from problems.minimum_window_substring import min_window


def test_example_1():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_example_2():
    assert min_window("a", "a") == "a"


def test_example_3():
    assert min_window("a", "aa") == ""


def test_example_ab():
    assert min_window("ab", "a") == "a"
