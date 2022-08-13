from problems.min_stack import MinStack


def assert_input_correct(instructions, values):
    stack: MinStack
    for instruction, value in zip(instructions, values):
        if instruction == "MinStack":
            stack = MinStack()
        elif instruction == "push":
            stack.push(value[0])
        elif instruction == "pop":
            assert stack.pop() == value[0]
        elif instruction == "top":
            assert stack.top() == value[0]
        elif instruction == "getMin":
            assert stack.get_min() == value[0]
        else:
            raise ValueError(f"instruction {instruction} is not valid")


def test_example_1():
    assert_input_correct(
        ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        [[], [-2], [0], [-3], [-3], [-3], [0], [-2]],
    )


def test_typical():
    assert_input_correct(
        [
            "MinStack",
            "push",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "getMin",
            "pop",
            "getMin",
            "pop",
            "getMin",
        ],
        [[], [2], [0], [3], [0], [0], [0], [0], [3], [0], [0], [2]],
    )


def test_large():
    assert_input_correct(
        [
            "MinStack",
            "push",
            "push",
            "push",
            "top",
            "pop",
            "getMin",
            "pop",
            "getMin",
            "pop",
            "push",
            "top",
            "getMin",
            "push",
            "top",
            "getMin",
            "pop",
            "getMin",
        ],
        [
            [],
            [2147483646],
            [2147483646],
            [2147483647],
            [2147483647],
            [2147483647],
            [2147483646],
            [2147483646],
            [2147483646],
            [2147483646],
            [2147483647],
            [2147483647],
            [2147483647],
            [-2147483648],
            [-2147483648],
            [-2147483648],
            [-2147483648],
            [2147483647],
        ],
    )


def test_negatives():
    assert_input_correct(
        [
            "MinStack",
            "push",
            "push",
            "getMin",
            "getMin",
            "push",
            "getMin",
            "getMin",
            "top",
            "getMin",
            "pop",
            "push",
            "push",
            "getMin",
            "push",
            "pop",
            "top",
            "getMin",
            "pop",
        ],
        [
            [],
            [-10],
            [14],
            [-10],
            [-10],
            [-20],
            [-20],
            [-20],
            [-20],
            [-20],
            [-20],
            [10],
            [-7],
            [-10],
            [-7],
            [-7],
            [-7],
            [-10],
            [-7],
        ],
    )


def test_repeats():
    assert_input_correct(
        ["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"],
        [[], [-2], [0], [-1], [-2], [-1], [-1], [-2]],
    )
