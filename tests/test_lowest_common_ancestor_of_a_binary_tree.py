from definitions.tree_node import TreeNode
from problems.lowest_common_ancestor_of_a_binary_tree import (
    lowest_common_ancestor,
)


def test_example_1():
    root = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.find(5)
    q = root.find(1)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(3)


def test_example_2():
    root = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.find(5)
    q = root.find(4)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(5)


def test_example_3():
    root = TreeNode.from_vals([1, 2])
    p = root.find(1)
    q = root.find(2)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(1)
