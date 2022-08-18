from typing import Optional

from definitions.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    row = [root] if root else []
    level = 0
    while row:
        row = [node for node in row for node in (node.left, node.right) if node]
        level += 1
    return level
