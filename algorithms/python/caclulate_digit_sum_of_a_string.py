def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        s = "".join(f"{sum(map(int, s[i:i + k]))}" for i in range(0, len(s), k))
    return s


def test_1():
    assert digit_sum("11111222223", 3) == "135"


def test_2():
    assert digit_sum("00000000", 3) == "000"
