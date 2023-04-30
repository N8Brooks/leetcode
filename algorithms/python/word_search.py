from collections import Counter
from itertools import chain
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # Efficiency from Solution tab answer was too good to pass up

    def search(row, col, i=0):
        if len(word) == i:
            return True

        if not 0 <= row < rows or not 0 <= col < cols or board[row][col] != word[i]:
            return False

        temp = board[row][col]
        board[row][col] = None
        found = (
            search(row - 1, col, i + 1)
            or search(row, col + 1, i + 1)
            or search(row + 1, col, i + 1)
            or search(row, col - 1, i + 1)
        )
        board[row][col] = temp
        return found

    rows = len(board)
    cols = len(board[0])
    word_dict = Counter(word)
    board_dict = Counter(chain.from_iterable(board))

    if any(count > board_dict[char] for char, count in word_dict.items()):
        return False

    if word_dict[word[0]] > word_dict[word[-1]]:
        word = word[::-1]

    return any(search(row, col) for row in range(rows) for col in range(cols))


def test_example_1() -> None:
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )


def test_example_2() -> None:
    assert (
        exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
        is True
    )


def test_example_3() -> None:
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
        is False
    )


def test_small() -> None:
    assert exist([["a", "a"]], "a") is True
