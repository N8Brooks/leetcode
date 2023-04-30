def kth_grammar(_: int, k: int) -> int:
    s = 0
    k -= 1
    while k:
        s ^= k & 1
        k >>= 1
    return s


def test_example_1():
    assert kth_grammar(1, 1) == 0


def test_example_2():
    assert kth_grammar(2, 1) == 0


def test_example_3():
    assert kth_grammar(2, 2) == 1


def test_3_3():
    assert kth_grammar(3, 3) == 1


def test_3_4():
    assert kth_grammar(3, 4) == 0
