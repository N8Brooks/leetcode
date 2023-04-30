from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    indegree = [0] * num_courses
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    for j, i in prerequisites:
        indegree[j] += 1
        graph[i].append(j)
    stack = [i for i in range(num_courses) if indegree[i] == 0]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                stack.append(j)
    return not any(indegree)


def test_example_1() -> None:
    assert can_finish(2, [[1, 0]]) is True


def test_example_2() -> None:
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_three() -> None:
    assert can_finish(3, [[1, 0], [1, 2], [0, 1]]) is False


def test_backwards() -> None:
    assert can_finish(2, [[0, 1]]) is True
