class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmentric_rec(root):

    if root is None:
        return True

    helper(root.left, root.right)


def helper(left, right):

    if left is None and right is None:
        return True

    if left is not None and right is not None and left.val != right.val:
        return False

    go_left = helper(left.left, right.right)
    go_right = helper(left.right, right.left)

    # return helper(left.left, right.right) and helper(left.right, right.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(5)
root.left.left.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(7)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(5)

ans = is_symmentric_rec(root)
