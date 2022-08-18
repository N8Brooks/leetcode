from typing import Optional

from definitions.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    row = [root] if root else []
    depth = 0
    while row:
        row = [node for node in row for node in (node.left, node.right) if node]
        depth += 1
    return depth
