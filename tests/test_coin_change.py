from problems.coin_change import coin_change


def test_example_1():
    assert coin_change([1, 2, 5], 11) == 3


def test_example_2():
    assert coin_change([2], 3) == -1


def test_example_3():
    assert coin_change([1], 0) == 0


def test_more():
    assert coin_change([1, 2, 5], 100) == 20


def test_most():
    assert coin_change([478, 487, 16, 338], 1990) == 15


def test_small():
    assert coin_change([2], 3) == -1


def test_obscure():
    assert coin_change([186, 419, 83, 408], 6249) == 20


def test_other():
    assert coin_change([3, 7, 405, 436], 8839) == 25


def test_larger():
    assert coin_change([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], 9999) == -1


def test_largest():
    assert (
        coin_change([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864)
        == 24
    )
