from string import hexdigits


def to_hex(num: int) -> str:
    if not num:
        return "0"
    if num < 0:
        num += 0x100000000
    digits = []
    while num:
        num, i = divmod(num, 16)
        digit = hexdigits[i]
        digits.append(digit)
    digits.reverse()
    return "".join(digits)


def test_case_1():
    assert to_hex(26) == "1a"


def test_case_2():
    assert to_hex(-1) == "ffffffff"


def test_0():
    assert to_hex(0) == "0"
