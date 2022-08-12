from definitions.tree_node import TreeNode
from problems.diameter_of_binary_tree import diameter_of_binary_tree


def test_example_1():
    assert diameter_of_binary_tree(TreeNode.from_vals([1, 2, 3, 4, 5])) == 3


def test_example_2():
    assert diameter_of_binary_tree(TreeNode.from_vals([1, 2])) == 1
