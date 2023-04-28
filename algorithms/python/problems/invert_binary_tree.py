from typing import Optional

from definitions.tree_node import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend((node.left, node.right))
    return root
