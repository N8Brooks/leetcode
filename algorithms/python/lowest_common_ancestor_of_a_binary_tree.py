from .definitions.tree_node import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root in (None, p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right


# mypy: ignore-errors


def test_example_1():
    root = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.find(5)
    q = root.find(1)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(3)


def test_example_2():
    root = TreeNode.from_vals([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = root.find(5)
    q = root.find(4)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(5)


def test_example_3():
    root = TreeNode.from_vals([1, 2])
    p = root.find(1)
    q = root.find(2)
    actual = lowest_common_ancestor(root, p, q)
    assert actual is root.find(1)
