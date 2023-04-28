from definitions.tree_node import TreeNode
from problems.kth_smallest_element_in_a_bst import kth_smallest


def test_example_1() -> None:
    root = TreeNode.from_vals([3, 1, 4, None, 2])
    assert kth_smallest(root, 1) == 1


def test_example_2() -> None:
    root = TreeNode.from_vals([5, 3, 6, 2, 4, None, None, 1])
    assert kth_smallest(root, 3) == 3
