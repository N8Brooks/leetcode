from definitions.tree_node import TreeNode
from problems.invert_binary_tree import invert_tree


def test_example_1():
    actual = invert_tree(TreeNode.from_vals([4, 2, 7, 1, 3, 6, 9]))
    assert actual.to_vals() == [4, 7, 2, 9, 6, 3, 1]


def test_example_2():
    actual = invert_tree(TreeNode.from_vals([2, 1, 3]))
    assert actual.to_vals() == [2, 3, 1]


def test_example_3():
    actual = invert_tree(None)
    assert actual.to_vals() if actual else [] == []
