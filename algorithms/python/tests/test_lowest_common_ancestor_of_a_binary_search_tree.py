from definitions.tree_node import TreeNode
from problems.lowest_common_ancestor_of_a_binary_search_tree import (
    lowest_common_ancestor,
)


def test_example_1() -> None:
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(8)
    assert lowest_common_ancestor(root, p, q).val == 6  # type: ignore


def test_example_2() -> None:
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(4)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore


def test_example_3() -> None:
    root = TreeNode.from_vals([2, 1])
    p = TreeNode(2)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore


def test_q_greater_than_p() -> None:
    root = TreeNode.from_vals([2, 1, 3])
    p = TreeNode(3)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore
