from definitions.tree_node import TreeNode
from problems.lowest_common_ancestor_of_a_binary_search_tree import (
    lowest_common_ancestor,
)


def test_example_1():
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(8)
    assert lowest_common_ancestor(root, p, q).val == 6


def test_example_2():
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(4)
    assert lowest_common_ancestor(root, p, q).val == 2


def test_example_3():
    root = TreeNode.from_vals([2, 1])
    p = TreeNode(2)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2


def test_q_greater_than_p():
    root = TreeNode.from_vals([2, 1, 3])
    p = TreeNode(3)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2
