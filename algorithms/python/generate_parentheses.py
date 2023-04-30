from typing import List


def generate_parenthesis(n: int) -> List[str]:
    table: List[List[str]] = [[] for _ in range(n + 1)]
    table[0].append("")
    for i in range(n + 1):
        for j in range(i):
            table[i].extend(f"({a}){b}" for b in table[j] for a in table[i - j - 1])
    return table[n]


def test_example_1():
    assert generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test_example_2():
    assert generate_parenthesis(1) == ["()"]
