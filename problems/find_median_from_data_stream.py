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
            self.max_heap[0]
            if len(self.max_heap) > len(self.min_heap)
            else (self.max_heap[0] - self.min_heap[0]) / 2
        )
