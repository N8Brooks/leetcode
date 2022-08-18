from problems.implement_trie_prefix_tree import Trie


def assert_input_correct(instructions, values):
    trie: Trie
    for instruction, value in zip(instructions, values):
        match instruction:
            case "Trie":
                trie = Trie()
            case "insert":
                trie.insert(value[0])
            case "search":
                assert trie.search(value[0]) == value[1]
            case "startsWith":
                assert trie.starts_with(value[0]) == value[1]
            case _:
                raise ValueError(f"Invalid instruction {instruction}")


def test_example_1() -> None:
    assert_input_correct(
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [
            [],
            ["apple"],
            ["apple", True],
            ["app", False],
            ["app", True],
            ["app"],
            ["app", True],
        ],
    )


def test_long() -> None:
    assert_input_correct(
        [
            "Trie",
            "insert",
            "startsWith",
            "search",
            "insert",
            "startsWith",
            "search",
            "insert",
            "startsWith",
            "search",
            "insert",
            "startsWith",
            "search",
            "insert",
            "startsWith",
            "search",
            "insert",
            "startsWith",
            "search",
        ],
        [
            [],
            ["p"],
            ["pr", False],
            ["p", True],
            ["pr"],
            ["pre", False],
            ["pr", True],
            ["pre"],
            ["pre", True],
            ["pre", True],
            ["pref"],
            ["pref", True],
            ["pref", True],
            ["prefi"],
            ["pref", True],
            ["prefi", True],
            ["prefix"],
            ["prefi", True],
            ["prefix", True],
        ],
    )


def test_empty() -> None:
    assert_input_correct(["Trie", "startsWith"], [[], ["a", False]])
