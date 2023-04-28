from math import factorial


def unique_paths(m: int, n: int) -> int:
    return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
