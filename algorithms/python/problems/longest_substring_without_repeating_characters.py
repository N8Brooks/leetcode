def length_of_longest_substring(s: str) -> int:
    i = length = 0
    for j, char in enumerate(s):
        i = max(i, s.rfind(char, i, j) + 1)
        length = max(length, j - i + 1)
    return length
