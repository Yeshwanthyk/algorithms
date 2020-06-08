"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""


def lca_bt_iter(root, p, q):

    parent = {root: None}
    stack = [root]

    # We use a dict to keep track of all root nodes and their parents
    while stack:

        root = stack.pop()
        if root.right:
            parent[root.right] = root
            root = root.right
        if root.left:
            parent[root.left] = root
            root = root.left

    ancestors = set()

    # Starting from `p` we find the path of `p` -> `root`
    while p:
        ancestors.add(p)
        p = parent[p]

    # we walk through `q` till where it coincides with the path
    # and that value is q
    while q not in p:
        q = parent[q]

    return q


def LCA_rec(root, p, q):

    if not root:
        return

    if p == root.val or q == root.val:
        return root

    left = LCA_rec(root, p, q)
    right = LCA_rec(root, p, q)

    if left and not right:
        return left

    if right and not left:
        return right

    if left and right:
        return root
