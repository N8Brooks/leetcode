from collections import deque

from definitions.tree_node import TreeNode

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
