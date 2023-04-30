from .definitions.tree_node import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    p, q = (q, p) if p.val > q.val else (p, q)
    while not p.val <= root.val <= q.val:
        root = root.left if root.val > p.val else root.right
    return root


def test_example_1() -> None:
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(8)
    assert lowest_common_ancestor(root, p, q).val == 6  # type: ignore


def test_example_2() -> None:
    root = TreeNode.from_vals([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = TreeNode(2)
    q = TreeNode(4)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore


def test_example_3() -> None:
    root = TreeNode.from_vals([2, 1])
    p = TreeNode(2)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore


def test_q_greater_than_p() -> None:
    root = TreeNode.from_vals([2, 1, 3])
    p = TreeNode(3)
    q = TreeNode(1)
    assert lowest_common_ancestor(root, p, q).val == 2  # type: ignore
