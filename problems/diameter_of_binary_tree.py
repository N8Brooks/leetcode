from definitions.tree_node import TreeNode


def diameter_of_binary_tree(root: TreeNode) -> int:
    def parse(root):
        nonlocal diameter
        if not root:
            return 0
        ldepth = parse(root.left)
        rdepth = parse(root.right)
        diameter = max(diameter, ldepth + rdepth)
        return max(ldepth, rdepth) + 1

    diameter = 0
    parse(root)
    return diameter
