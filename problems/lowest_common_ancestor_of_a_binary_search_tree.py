from definitions.tree_node import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    p, q = (q, p) if p.val > q.val else (p, q)
    while not p.val <= root.val <= q.val:
        root = root.left if root.val > p.val else root.right
    return root
