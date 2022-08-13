from math import inf


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = inf

    def push(self, val: int) -> None:
        self.stack.append((self.min, val))
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.min, val = self.stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def get_min(self) -> int:
        return self.min
