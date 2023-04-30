from typing import List, Optional

from .definitions.tree_node import TreeNode


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def get_node(start, end):
        if start > end:
            return None
        val = next(queue)
        node = TreeNode(val)
        i = lookup[val]
        node.left = get_node(start, i - 1)
        node.right = get_node(i + 1, end)
        return node

    queue = iter(preorder)
    lookup = {node: i for i, node in enumerate(inorder)}
    return get_node(0, len(inorder) - 1)


def test_example_1() -> None:
    actual = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).to_vals()  # type: ignore
    expected = [3, 9, 20, None, None, 15, 7]
    assert actual == expected


def test_example_2() -> None:
    assert build_tree([-1], [-1]).to_vals() == [-1]  # type: ignore
