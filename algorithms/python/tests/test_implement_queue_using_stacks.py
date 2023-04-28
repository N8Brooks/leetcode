from problems.implement_queue_using_stacks import MyQueue


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
