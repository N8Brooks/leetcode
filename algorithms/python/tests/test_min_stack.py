from problems.min_stack import MinStack


def assert_input_correct(instructions, values):
    stack: MinStack
    for instruction, value in zip(instructions, values):
        match instruction:
            case "MinStack":
                stack = MinStack()
            case "push":
                stack.push(value[0])
            case "pop":
                assert stack.pop() == value[0]
            case "top":
                assert stack.top() == value[0]
            case "getMin":
                assert stack.get_min() == value[0]
            case _:
                raise ValueError(f"instruction {instruction} is not valid")


def test_example_1() -> None:
    assert_input_correct(
        ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        [[], [-2], [0], [-3], [-3], [-3], [0], [-2]],
    )


def test_typical() -> None:
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


def test_large() -> None:
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


def test_negatives() -> None:
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


def test_repeats() -> None:
    assert_input_correct(
        ["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"],
        [[], [-2], [0], [-1], [-2], [-1], [-1], [-2]],
    )
