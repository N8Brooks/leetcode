from itertools import islice
from typing import Generator, Optional

from definitions.tree_node import TreeNode


def inorder_traversal(node: Optional[TreeNode]) -> Generator[TreeNode, None, None]:
    stack = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        yield node
        node = node.right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    return next(islice(inorder_traversal(root), k - 1, None)).val
