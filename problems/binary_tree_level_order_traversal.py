from typing import List, Optional

from definitions.tree_node import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    level = [root] if root else []
    result = []
    while level:
        result.append([node.val for node in level])
        level = [node for node in level for node in (node.left, node.right) if node]
    return result
