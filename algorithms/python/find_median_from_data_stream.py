from heapq import heappop, heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num) -> None:
        heappush(self.min_heap, -heappushpop(self.max_heap, num))
        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self) -> float:
        return (
            float(self.max_heap[0])
            if len(self.max_heap) > len(self.min_heap)
            else (self.max_heap[0] - self.min_heap[0]) / 2
        )


def assert_input_correct(instructions, values):
    finder: MedianFinder
    for instruction, value in zip(instructions, values):
        match instruction:
            case "MedianFinder":
                finder = MedianFinder()
            case "addNum":
                finder.add_num(value[0])
            case "findMedian":
                assert finder.find_median() == value[0]
            case _:
                raise ValueError(f"{instruction} is not a valid instruction")


def test_example_1() -> None:
    assert_input_correct(
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [1.5], [3], [2]],
    )


def test_one() -> None:
    assert_input_correct(["MedianFinder", "addNum", "findMedian"], [[], [1], [1]])
