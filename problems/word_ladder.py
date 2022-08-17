from string import ascii_lowercase
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    word_list = set(word_list)
    if end_word not in word_list:
        return 0
    knapsack_1 = {begin_word}
    knapsack_2 = {end_word}
    transformations = 1
    while knapsack_1:
        word_list -= knapsack_1
        knapsack_1 = word_list.intersection(
            f"{word[:i]}{letter}{word[i + 1:]}"
            for word in knapsack_1
            for i in range(len(word))
            for letter in ascii_lowercase
        )
        transformations += 1
        if not knapsack_1.isdisjoint(knapsack_2):
            return transformations
        if len(knapsack_1) > len(knapsack_2):
            knapsack_1, knapsack_2 = knapsack_2, knapsack_1
    return 0
