from problems.implement_queue_using_stacks import MyQueue


def assert_input_correct(instructions, values):
    queue: MyQueue
    for instruction, value in zip(instructions, values):
        if instruction == "MyQueue":
            queue = MyQueue()
        elif instruction == "push":
            queue.push(value[0])
        elif instruction == "pop":
            assert queue.pop() == value[0]
        elif instruction == "peek":
            assert queue.peek() == value[0]
        elif instruction == "empty":
            assert queue.empty() == value[0]
        else:
            raise ValueError(f"Instruction {instruction} not valid")


def test_example_1():
    assert_input_correct(
        ["MyQueue", "push", "push", "peek", "pop", "empty"],
        [[], [1], [2], [1], [1], [False]],
    )
