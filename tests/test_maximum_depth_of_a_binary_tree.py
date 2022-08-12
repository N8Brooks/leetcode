from definitions.tree_node import TreeNode
from problems.maximum_depth_of_a_binary_tree import max_depth


def test_example_1():
    assert max_depth(TreeNode.from_vals([3, 9, 20, None, None, 15, 7])) == 3


def test_example_2():
    assert max_depth(TreeNode.from_vals([1, None, 2])) == 2
