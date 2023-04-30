from typing import Optional

from .definitions.tree_node import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend((node.left, node.right))
    return root


def test_example_1() -> None:
    actual = invert_tree(TreeNode.from_vals([4, 2, 7, 1, 3, 6, 9]))
    assert actual.to_vals() == [4, 7, 2, 9, 6, 3, 1]  # type: ignore


def test_example_2() -> None:
    actual = invert_tree(TreeNode.from_vals([2, 1, 3]))
    assert actual.to_vals() == [2, 3, 1]  # type: ignore


def test_example_3() -> None:
    actual = invert_tree(None)
    assert actual.to_vals() if actual else [] == []  # type: ignore
