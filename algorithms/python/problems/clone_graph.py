from typing import Optional

from definitions.node import Node


def clone_graph(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return root

    nodes = {}
    stack = [root]

    # Clone values
    while stack:
        node = stack.pop()
        nodes[node] = Node(node.val, node.neighbors)
        for neighbor in node.neighbors:
            if neighbor not in nodes:
                stack.append(neighbor)

    # Clone neighbors
    for node in nodes.values():
        node.neighbors = [nodes[neighbor] for neighbor in node.neighbors]

    return nodes[root]
