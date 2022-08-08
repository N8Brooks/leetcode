from __future__ import annotations

from itertools import chain
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_vals(vals: List[int]) -> Optional[TreeNode]:
        def helper(i: int):
            if i >= len(vals) or vals[i] is None:
                return None
            node = TreeNode(vals[i])
            node.left = helper(2 * i + 1)
            node.right = helper(2 * i + 2)
            return node

        return helper(0)

    def to_vals(self) -> List[int]:
        result = []
        nodes = [self]
        while any(nodes):
            result.extend(node.val for node in nodes)
            temp = ((node.left, node.right) if node else (None, None) for node in nodes)
            nodes = tuple(chain.from_iterable(temp))
        return result
