from typing import List, Optional

from .definitions.tree_node import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    level = [root] if root else []
    result = []
    while level:
        result.append([node.val for node in level])
        level = [node for node in level for node in (node.left, node.right) if node]
    return result


def test_example_1() -> None:
    root = TreeNode.from_vals([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_example_2() -> None:
    root = TreeNode.from_vals([1])
    assert level_order(root) == [[1]]


def test_example_3() -> None:
    assert not level_order(None)
