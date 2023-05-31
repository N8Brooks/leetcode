from itertools import accumulate, takewhile
from typing import List


class TreeAncestor:  # pylint: disable=too-few-public-methods
    def __init__(self, _: int, parent: List[int]):
        self.parents = list(
            accumulate(
                range((50_000).bit_length()),
                lambda parent, _: [
                    parent[node] if node > -1 else -1 for node in parent
                ],
                initial=parent,
            )
        )

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for parent in takewhile(lambda _: k and node > -1, self.parents):
            if k & 1:
                node = parent[node]
            k >>= 1
        return node


def test_example_1():
    tree_ancestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    assert tree_ancestor.get_kth_ancestor(3, 1) == 1
    assert tree_ancestor.get_kth_ancestor(5, 2) == 0
    assert tree_ancestor.get_kth_ancestor(6, 3) == -1


def test_example_2():
    tree_ancestor = TreeAncestor(5, [-1, 0, 0, 0, 3])
    assert tree_ancestor.get_kth_ancestor(1, 5) == -1
    assert tree_ancestor.get_kth_ancestor(3, 2) == -1
    assert tree_ancestor.get_kth_ancestor(0, 1) == -1
    assert tree_ancestor.get_kth_ancestor(3, 1) == 0
    assert tree_ancestor.get_kth_ancestor(3, 5) == -1
