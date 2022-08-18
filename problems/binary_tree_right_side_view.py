from typing import List, Optional

from definitions.tree_node import TreeNode


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result = []
    row = [root] if root else []
    while row:
        result.append(row[-1].val)
        row = [node for node in row for node in (node.left, node.right) if node]
    return result
