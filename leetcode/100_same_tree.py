"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if (not p and q) or (not q and p):
            return False

        if not p and not q:
            return True

        p_array = self.pre_order(p)
        q_array = self.pre_order(q)

        if p_array == q_array:
            return True
        else:
            return False

    def pre_order(self, root):

        ret = []

        if not root:
            return ret.append(None)

        ret.append(root.val)
        if root.left:
            ret += self.pre_order(root.left)
        if root.right:
            ret += self.pre_order(root.right)

        return ret


p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(None)
q.right = TreeNode(2)

s = Solution()

ans = s.isSameTree(p, q)
print(ans)
