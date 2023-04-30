from math import inf
from typing import List, Optional

from .definitions.tree_node import TreeNode


def is_valid_bst(node: Optional[TreeNode]) -> bool:
    stack: List[TreeNode] = []
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


def test_example_1() -> None:
    assert is_valid_bst(TreeNode.from_vals([2, 1, 3])) is True


def test_example_2() -> None:
    assert is_valid_bst(TreeNode.from_vals([5, 1, 4, None, None, 3, 6])) is False


def test_replicates() -> None:
    assert is_valid_bst(TreeNode.from_vals([2, 2, 2])) is False


def test_snake_eyes() -> None:
    assert is_valid_bst(TreeNode.from_vals([1, 1])) is False


def test_random() -> None:
    assert is_valid_bst(TreeNode.from_vals([5, 4, 6, None, None, 3, 7])) is False


def test_empty() -> None:
    assert is_valid_bst(None) is True


def test_large() -> None:
    assert (
        is_valid_bst(TreeNode.from_vals([32, 26, 47, 19, None, None, 56, None, 27]))
        is False
    )
