from definitions.tree_node import TreeNode
from problems.balanced_binary_tree import is_balanced


def test_example_1():
    assert is_balanced(TreeNode.from_vals([3, 9, 20, None, None, 15, 7])) is True


def test_example_2():
    assert is_balanced(TreeNode.from_vals([1, 2, 2, 3, 3, None, None, 4, 4])) is False


def test_example_3():
    assert is_balanced(None) is True
