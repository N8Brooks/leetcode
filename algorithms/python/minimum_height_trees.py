from typing import List, Set


def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    adj: List[Set[int]] = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    leaves = [i for i, nodes in enumerate(adj) if len(nodes) == 1]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1:
                new_leaves.append(j)
        leaves = new_leaves
    return leaves


def test_example_1() -> None:
    assert find_min_height_trees(4, [[1, 0], [1, 2], [1, 3]]) == [1]


def test_example_2() -> None:
    assert find_min_height_trees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4]


def test_empty() -> None:
    assert find_min_height_trees(1, []) == [0]
