from typing import Optional

from definitions.tree_node import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
