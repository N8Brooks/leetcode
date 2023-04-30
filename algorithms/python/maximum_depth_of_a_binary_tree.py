from typing import Optional

from .definitions.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    depth = 0
    level = [root] if root else []
    while level:
        depth += 1
        level = [node for node in level for node in (node.left, node.right) if node]
    return depth


def test_example_1() -> None:
    assert max_depth(TreeNode.from_vals([3, 9, 20, None, None, 15, 7])) == 3


def test_example_2() -> None:
    assert max_depth(TreeNode.from_vals([1, None, 2])) == 2
