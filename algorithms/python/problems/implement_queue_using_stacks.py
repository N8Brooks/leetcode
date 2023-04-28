class MyQueue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def ground(self) -> None:
        if not self.queue:
            self.queue.extend(reversed(self.stack))
            self.stack.clear()

    def pop(self) -> int:
        self.ground()
        return self.queue.pop()

    def peek(self) -> int:
        self.ground()
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue and not self.stack
