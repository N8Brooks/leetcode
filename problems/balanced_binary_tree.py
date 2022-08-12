from typing import Optional

from definitions.tree_node import TreeNode


def is_balanced(node: Optional[TreeNode]) -> bool:
    stack = []
    last = None
    depths = {}
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack[-1]
        if node.right and last is not node.right:
            node = node.right
        else:
            last = node = stack.pop()
            ldepth = depths.get(node.left, 0)
            rdepth = depths.get(node.right, 0)
            if not -1 <= ldepth - rdepth <= 1:
                return False
            depths[node] = max(ldepth, rdepth) + 1
            node = None
    return True
