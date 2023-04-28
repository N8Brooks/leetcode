from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        group = "".join(sorted(word))
        groups[group].append(word)
    return list(groups.values())
