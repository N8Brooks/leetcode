from typing import Generator, List


def max_areas(height: List[int]) -> Generator[int, None, None]:
    i = 0
    j = len(height) - 1
    while i < j:
        if height[i] < height[j]:
            yield (j - i) * height[i]
            i += 1
        else:
            yield (j - i) * height[j]
            j -= 1


def max_area(height: List[int]) -> int:
    return max(max_areas(height), default=0)


def test_example_1() -> None:
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2() -> None:
    assert max_area([1, 1]) == 1
