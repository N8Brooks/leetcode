from problems.construct_binary_tree_from_preorder_and_inorder_traversal import (
    build_tree,
)


def test_example_1() -> None:
    actual = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).to_vals()  # type: ignore
    expected = [3, 9, 20, None, None, 15, 7]
    assert actual == expected


def test_example_2() -> None:
    assert build_tree([-1], [-1]).to_vals() == [-1]  # type: ignore
