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


def assert_input_correct(instructions, values):
    queue: MyQueue
    for instruction, value in zip(instructions, values):
        match instruction:
            case "MyQueue":
                queue = MyQueue()
            case "push":
                queue.push(value[0])
            case "pop":
                assert queue.pop() == value[0]
            case "peek":
                assert queue.peek() == value[0]
            case "empty":
                assert queue.empty() == value[0]
            case _:
                raise ValueError(f"Instruction {instruction} not valid")


def test_example_1() -> None:
    assert_input_correct(
        ["MyQueue", "push", "push", "peek", "pop", "empty"],
        [[], [1], [2], [1], [1], [False]],
    )
