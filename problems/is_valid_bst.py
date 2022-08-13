from math import inf
from typing import Optional

from definitions.tree_node import TreeNode


def is_valid_bst(node: Optional[TreeNode]) -> bool:
    stack = []
    last = TreeNode(-inf)
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if last.val >= node.val:
            return False
        last, node = node, node.right
    return True
