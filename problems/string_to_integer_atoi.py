import re

PATTERN = re.compile(r"\s*([-+]?\d+)")

LO = -(2**31)

HI = 2**31 - 1


def my_atoi(s: str) -> int:
    match = PATTERN.match(s)
    return max(LO, min(HI, int(match[0]))) if match else 0
