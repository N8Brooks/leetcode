from problems.find_median_from_data_stream import MedianFinder


def assert_input_correct(instructions, values):
    finder: MedianFinder
    for instruction, value in zip(instructions, values):
        if instruction == "MedianFinder":
            finder = MedianFinder()
        elif instruction == "addNum":
            finder.add_num(value[0])
        elif instruction == "findMedian":
            assert finder.find_median() == value[0]
        else:
            raise ValueError(f"{instruction} is not a valid instruction")


def test_example_1() -> None:
    assert_input_correct(
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [1.5], [3], [2]],
    )


def test_one() -> None:
    assert_input_correct(["MedianFinder", "addNum", "findMedian"], [[], [1], [1]])
