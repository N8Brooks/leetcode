from typing import Optional

from definitions.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    def parse(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        ldepth = parse(node.left)
        rdepth = parse(node.right)
        return max(ldepth, rdepth) + 1

    return parse(root)
