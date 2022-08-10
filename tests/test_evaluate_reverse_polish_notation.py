from problems.evaluate_reverse_polish_notation import eval_rpn


def test_example_1():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_example_2():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_example_3():
    assert (
        eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )


def test_minus():
    assert eval_rpn(["4", "3", "-"]) == 1
