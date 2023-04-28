from itertools import islice
from typing import Generator, Iterable, List, Optional

from definitions.tree_node import TreeNode


def inorder_traversal(node: Optional[TreeNode]) -> Generator[TreeNode, None, None]:
    stack: List[TreeNode] = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        yield node
        node = node.right


def nth(iterable: Iterable[TreeNode], n: int) -> TreeNode:
    """Based on itertools `nth()` recipe"""
    return next(islice(iterable, n, None))


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    return nth(inorder_traversal(root), k - 1).val
