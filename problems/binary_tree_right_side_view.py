from collections import deque
from typing import List, Optional

from definitions.tree_node import TreeNode


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []
    queue = deque([root] if root else [])
    while queue:
        result.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
