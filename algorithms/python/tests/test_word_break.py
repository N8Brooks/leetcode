from problems.word_break import word_break


def test_example_1() -> None:
    assert word_break("leetcode", ["leet", "code"]) is True


def test_example_2() -> None:
    assert word_break("applepenapple", ["apple", "pen"]) is True


def test_example_3() -> None:
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_long() -> None:
    assert (
        word_break(
            "bccdbacdbdacddabbaaaadababadad",
            [
                "cbc",
                "bcda",
                "adb",
                "ddca",
                "bad",
                "bbb",
                "dad",
                "dac",
                "ba",
                "aa",
                "bd",
                "abab",
                "bb",
                "dbda",
                "cb",
                "caccc",
                "d",
                "dd",
                "aadb",
                "cc",
                "b",
                "bcc",
                "bcd",
                "cd",
                "cbca",
                "bbd",
                "ddd",
                "dabb",
                "ab",
                "acd",
                "a",
                "bbcc",
                "cdcbd",
                "cada",
                "dbca",
                "ac",
                "abacd",
                "cba",
                "cdb",
                "dbac",
                "aada",
                "cdcda",
                "cdc",
                "dbc",
                "dbcb",
                "bdb",
                "ddbdd",
                "cadaa",
                "ddbc",
                "babb",
            ],
        )
        is True
    )
