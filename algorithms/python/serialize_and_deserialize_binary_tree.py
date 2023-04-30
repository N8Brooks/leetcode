from collections import deque

from .definitions.tree_node import TreeNode

# Some creative liberties were taken around "null"


class Codec:
    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(f"{node.val}")
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("")

        while result[-1] == "":
            del result[-1]

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        nodes = [TreeNode(None if val == "" else int(val)) for val in data.split(",")]
        for i, node in enumerate(nodes):
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]

        return nodes[0]


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
