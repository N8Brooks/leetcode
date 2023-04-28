from typing import Optional

from definitions.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    depth = 0
    level = [root] if root else []
    while level:
        depth += 1
        level = [node for node in level for node in (node.left, node.right) if node]
    return depth
