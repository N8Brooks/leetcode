from typing import List


def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    adj = [set() for _ in range(n)]
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
