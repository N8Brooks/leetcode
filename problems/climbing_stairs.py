PHI = (5**0.5 + 1) / 2


def climb_stairs(n: int) -> int:
    # Based on O(1) fibonacci solution
    return round(PHI ** (n + 1) / 5**0.5)
