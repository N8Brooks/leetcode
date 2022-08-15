from __future__ import annotations

from typing import List, Optional


class Node:  # pylint: disable=too-few-public-methods
    """Definition for a Node"""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @staticmethod
    def from_adj_list(adj_list: List[List[int]]) -> Optional[Node]:
        """First `Node` from a graph constructed from an adjacency list"""
        nodes = [Node(i + 1) for i in range(len(adj_list))]
        for node, neighbors in zip(nodes, adj_list):
            node.neighbors = [nodes[val - 1] for val in neighbors]
        return nodes and nodes[0]
