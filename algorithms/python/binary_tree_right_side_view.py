from typing import List, Optional

from .definitions.tree_node import TreeNode


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []
    row = [root] if root else []
    while row:
        result.append(row[-1].val)
        row = [node for node in row for node in (node.left, node.right) if node]
    return result


def test_example_1() -> None:
    assert right_side_view(TreeNode.from_vals([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]


def test_example_2() -> None:
    assert right_side_view(TreeNode.from_vals([1, None, 3])) == [1, 3]


def test_example_3() -> None:
    assert not right_side_view(TreeNode.from_vals([]))


def test_one_two() -> None:
    assert right_side_view(TreeNode.from_vals([1, 2])) == [1, 2]


def test_one_to_four() -> None:
    assert right_side_view(TreeNode.from_vals([1, 2, 3, 4])) == [1, 3, 4]
