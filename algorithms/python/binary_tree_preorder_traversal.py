from typing import List, Optional

from .definitions.tree_node import TreeNode


def preorder_traversal(node: Optional[TreeNode]) -> List[int]:
    if not node:
        return []
    stack = [node]
    array = []
    while stack:
        node = stack.pop()
        array.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return array


def test_example_1():
    assert preorder_traversal(TreeNode.from_vals([1, None, 2, None, None, 3])) == [
        1,
        2,
        3,
    ]


def test_example_2():
    assert not preorder_traversal(TreeNode.from_vals([]))


def test_example_3():
    assert preorder_traversal(TreeNode.from_vals([1])) == [1]
