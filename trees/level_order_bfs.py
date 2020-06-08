class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):

    if not root:
        return []

    ret = []
    level = [root]

    while level and root:

        current_nodes = []
        next_nodes = []

        for node in level:
            current_nodes.append(node.val)
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        ret.append(current_nodes)

        level = next_nodes

    return ret


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

    ans = level_order(n1)
    print(ans)
