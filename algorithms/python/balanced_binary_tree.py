from typing import Dict, List, Optional

from .definitions.tree_node import TreeNode


def is_balanced(node: Optional[TreeNode]) -> bool:
    stack: List[TreeNode] = []
    last = None
    depths: Dict[TreeNode, int] = {}
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack[-1]
        if node.right and last is not node.right:
            node = node.right
        else:
            last = node = stack.pop()
            ldepth = depths.get(node.left, 0)
            rdepth = depths.get(node.right, 0)
            if not -1 <= ldepth - rdepth <= 1:
                return False
            depths[node] = max(ldepth, rdepth) + 1
            node = None
    return True


def test_example_1() -> None:
    assert is_balanced(TreeNode.from_vals([3, 9, 20, None, None, 15, 7])) is True


def test_example_2() -> None:
    assert is_balanced(TreeNode.from_vals([1, 2, 2, 3, 3, None, None, 4, 4])) is False


def test_example_3() -> None:
    assert is_balanced(None) is True
