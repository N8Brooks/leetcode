from definitions.tree_node import TreeNode
from problems.serialize_and_deserialize_binary_tree import Codec


# mypy: ignore-errors
def test_example_1() -> None:
    codec = Codec()
    root = TreeNode.from_vals([1, 2, 3, None, None, 4, 5])
    actual = codec.deserialize(codec.serialize(root)).to_vals()
    expected = [1, 2, 3, None, None, 4, 5]
    assert actual == expected


def test_example_2() -> None:
    codec = Codec()
    root = None
    actual = codec.deserialize(codec.serialize(root))
    assert actual is None


def test_long() -> None:
    codec = Codec()
    root = TreeNode.from_vals([1, 2, 3, -1, -1, 4, 5, 6, 7])
    two = root.find(2)
    two.left.val = two.right.val = ""
    actual = codec.deserialize(codec.serialize(root)).to_vals()
    expected = [1, 2, 3, None, None, 4, 5, 6, 7]
    assert actual == expected
