def word_break(s, words):
    breaks = [True] + [False] * len(s)
    for i, is_break in enumerate(breaks):
        if not is_break:
            continue
        for word in words:
            if s[i : i + len(word)] == word:
                breaks[i + len(word)] = True
    return breaks[-1]
