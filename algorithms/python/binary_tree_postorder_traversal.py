from typing import List, Optional

from .definitions.tree_node import TreeNode


def postorder_traversal(node: Optional[TreeNode]) -> List[int]:
    stack: List[TreeNode] = []
    array = []
    last = None
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        peek = stack[-1]
        if peek.right and last is not peek.right:
            node = peek.right
        else:
            array.append(peek.val)
            last = stack.pop()
    return array


def test_example_1():
    assert postorder_traversal(TreeNode.from_vals([1, None, 2, None, None, 3])) == [
        3,
        2,
        1,
    ]


def test_example_2():
    assert not postorder_traversal(TreeNode.from_vals([]))


def test_example_3():
    assert postorder_traversal(TreeNode.from_vals([1])) == [1]
