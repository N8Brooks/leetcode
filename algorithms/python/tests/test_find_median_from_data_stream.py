from problems.find_median_from_data_stream import MedianFinder


def assert_input_correct(instructions, values):
    finder: MedianFinder
    for instruction, value in zip(instructions, values):
        match instruction:
            case "MedianFinder":
                finder = MedianFinder()
            case "addNum":
                finder.add_num(value[0])
            case "findMedian":
                assert finder.find_median() == value[0]
            case _:
                raise ValueError(f"{instruction} is not a valid instruction")


def test_example_1() -> None:
    assert_input_correct(
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [2], [1.5], [3], [2]],
    )


def test_one() -> None:
    assert_input_correct(["MedianFinder", "addNum", "findMedian"], [[], [1], [1]])
