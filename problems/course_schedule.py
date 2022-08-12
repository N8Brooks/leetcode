from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    indegree = [0] * num_courses
    graph = [[] for _ in range(num_courses)]
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
