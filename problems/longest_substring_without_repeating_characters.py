def length_of_longest_substring(s: str) -> int:
    i = j = 0
    length = 0
    while j < len(s):
        while s.find(s[j], i, j) != -1:
            i += 1
        j += 1
        length = max(length, j - i)
    return length
