from typing import Dict, Optional

from definitions.node import Node
from problems.clone_graph import clone_graph


def to_adj_list(graph: Optional[Node]) -> Dict[int, Node]:
    nodes = {}
    stack = [graph] if graph else []
    while stack:
        node = stack.pop()
        nodes[node.val] = node
        for neighbor in node.neighbors:
            if neighbor.val not in nodes:
                stack.append(neighbor)
    return nodes


def assert_nodes_equal(actual_root: Optional[Node], expected_root: Optional[Node]):
    actual_graph = to_adj_list(actual_root)
    expected_graph = to_adj_list(expected_root)
    for expected in expected_graph.values():
        actual = actual_graph[expected.val]
        assert actual is not expected
        assert actual.val == expected.val


def test_example_1() -> None:
    root = Node.from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
    actual = clone_graph(root)
    expected = Node.from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
    assert_nodes_equal(actual, expected)


def test_example_2() -> None:
    root = Node.from_adj_list([[]])
    actual = clone_graph(root)
    expected = Node.from_adj_list([[]])
    assert_nodes_equal(actual, expected)


def test_example_3() -> None:
    assert clone_graph(None) is None
