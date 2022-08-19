from typing import Iterable, List


def is_valid(cells: Iterable[str]):
    nums = [cell for cell in cells if cell != "."]
    return len(nums) == len(set(nums))


def sub_boxes(board: List[List[str]]) -> Iterable[Iterable[str]]:
    return (
        (board[y + dy][x + dx] for dy in range(3) for dx in range(3))
        for x in range(0, 9, 3)
        for y in range(0, 9, 3)
    )


def is_valid_sudoku(board: List[List[str]]) -> bool:
    return (
        all(map(is_valid, board))
        and all(map(is_valid, zip(*board)))
        and all(map(is_valid, sub_boxes(board)))
    )
