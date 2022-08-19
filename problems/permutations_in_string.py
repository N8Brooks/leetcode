from collections import Counter


def check_inclusion(s_1: str, s_2: str) -> bool:
    counts = Counter(s_1)
    counts.subtract(s_2[: len(s_1)])
    if not any(counts.values()):
        return True
    for i, char in enumerate(s_2[len(s_1) :]):
        counts[char] -= 1
        counts[s_2[i]] += 1
        if not any(counts.values()):
            return True
    return False
