from typing import List


def word_break(s: str, word_dict: List(str)) -> bool:
    breaks = [True] + [False] * len(s)
    for i, is_break in enumerate(breaks):
        if not is_break:
            continue
        for word in word_dict:
            if s[i : i + len(word)] == word:
                breaks[i + len(word)] = True
    return breaks[-1]
