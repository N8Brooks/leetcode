from typing import List, Optional

from .definitions.tree_node import TreeNode


def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
    stack: List[TreeNode] = []
    array: List[int] = []
    while node or stack:  # pylint:disable=duplicate-code
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        array.append(node.val)
        node = node.right
    return array


def test_example_1():
    assert inorder_traversal(TreeNode.from_vals([1, None, 2, None, None, 3])) == [
        1,
        3,
        2,
    ]


def test_example_2():
    assert not inorder_traversal(TreeNode.from_vals([]))


def test_example_3():
    assert inorder_traversal(TreeNode.from_vals([1])) == [1]
