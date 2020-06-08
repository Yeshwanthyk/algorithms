"""
652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
"""

from collections import defaultdict


def find_dup(root):

    dic = defaultdict(int)
    ans = []

    def process_tree(root):

        if not root:
            return '#'

        print(f"Node : {root.val}")

        serial = str(root.val)

        left = process_tree(root.left)
        right = process_tree(root.right)

        serial += left + right

        # serial = "{}{}{}".format(root.val, process_tree(
        # root.left), process_tree(root.right))
        print(serial)

        dic[serial] += 1

        if dic[serial] == 2:
            ans.append(root)

        return serial

    process_tree(root)
    return ans


class Node:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


A = Node(1)
A.left = Node(2)
A.right = Node(4)
A.left.right = Node(4)

ans = find_dup(A)
print(ans)
