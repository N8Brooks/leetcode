from typing import Optional

from .definitions.tree_node import TreeNode


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    def parse(root):
        nonlocal diameter
        if not root:
            return 0
        ldepth = parse(root.left)
        rdepth = parse(root.right)
        diameter = max(diameter, ldepth + rdepth)
        return max(ldepth, rdepth) + 1

    diameter = 0
    parse(root)
    return diameter


def test_example_1() -> None:
    assert diameter_of_binary_tree(TreeNode.from_vals([1, 2, 3, 4, 5])) == 3


def test_example_2() -> None:
    assert diameter_of_binary_tree(TreeNode.from_vals([1, 2])) == 1
