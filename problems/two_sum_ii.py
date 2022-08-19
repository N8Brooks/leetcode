from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1
    while numbers[i] + numbers[j] != target:
        if numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return [i + 1, j + 1]
