from problems.word_ladder import ladder_length


def test_example_1() -> None:
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5


def test_example_2() -> None:
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0


def test_hot_dog() -> None:
    assert ladder_length("hot", "dog", ["hot", "dog"]) == 0


def test_a_b_c() -> None:
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2


def test_loop() -> None:
    assert ladder_length("hit", "cog", ["hot", "dot", "tog", "cog"]) == 0
