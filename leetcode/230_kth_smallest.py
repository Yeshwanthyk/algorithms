"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest_rec(root, k):

    if not root or k < 1:
        return

    res = []
    inorder_rec(root, k, res)
    return res[0]


def inorder_rec(root, k, res):

    if not root or len(res) > 0:
        return

    inorder_rec(root.left, k, res)

    k -= 1
    if k == 0:
        res.append(root.val)
        return

    inorder_rec(root.right, k, res)


def kth_smallest_iter(root, k):

    stack = []

    while stack or root:

        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        k -= 1

        if k == 0:
            break

        root = root.right

    return root.val


root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

ans = kth_smallest(root, 2)
print(ans)
