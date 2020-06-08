class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


"""
in_order: LDR
pre_order: DLR
post_order: LRD
"""


def in_order_rec(root):

    if not root:
        return []

    res = []

    res = in_order_rec(root.left)
    res.append(root.data)
    res = res + in_order_rec(root.right)

    return res


def in_order_iter(root):

    if not root:
        return []

    res = []
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        res.append(root.data)

        root = root.right

    return res


if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    print(in_order_rec(n1))
