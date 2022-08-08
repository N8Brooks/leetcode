from problems.invert_binary_tree import TreeNode, invert_tree


def from_list(vals):
    nodes = [None if val is None else TreeNode(val) for val in vals]
    for i in range(1, len(vals)):
        node = nodes[i]
        if node is None:
            continue
        parent = nodes[i // 2]
        if i % 2:
            parent.left = node
        else:
            parent.right = node
    return nodes and nodes[0]


def matches(a, b):
    if a is None or b is None:
        return a == b
    elif a.val != b.val:
        return False
    else:
        return matches(a.left, b.left) and matches(a.right, b.right)


def test_example_1():
    actual = invert_tree(from_list([4, 2, 7, 1, 3, 6, 9]))
    expected = from_list(
        [
            4,
            7,
            2,
            9,
            6,
            3,
        ]
    )
    assert matches(actual, expected)


def test_example_2():
    assert to_list(invert_tree(from_list([2, 1, 3]))) == [2, 3, 1]


def test_example_3():
    assert to_list(invert_tree(from_list([]))) == []
