PHI = (5**0.5 + 1) / 2

SQRT_5 = 5**0.5


def climb_stairs(n: int) -> int:
    return round(PHI ** (n + 1) / SQRT_5)
