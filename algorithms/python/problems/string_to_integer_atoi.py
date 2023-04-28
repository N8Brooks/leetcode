import re

PATTERN = re.compile(r"\s*([-+]?\d+)")


def my_atoi(s: str) -> int:
    match = PATTERN.match(s)
    return max(-(2**31), min(2**31 - 1, int(match[0]))) if match else 0
