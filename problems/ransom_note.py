from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    return Counter(magazine) >= Counter(ransom_note)
