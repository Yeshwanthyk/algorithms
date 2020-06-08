"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""


class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def serialize(root):

    def doit(node):
        if not node:
            return res.append("#")

        res.append(str(node.val))
        doit(node.left)
        doit(node.right)

    res = []
    doit(root)
    return ' '.join(res)


def deserialize(serialized_string):

    serialized_string = serialized_string.split(" ")
    return deserialize_helper(serialized_string)


def deserialize_helper(s_list):

    if len(s_list) == 0:
        return

    val = s_list.pop(0)

    if val is None or val is '#':
        return

    new_node = TreeNode(val)
    new_node.left = deserialize_helper(s_list)
    new_node.right = deserialize_helper(s_list)

    return new_node


# A = TreeNode('A')
# A.left = TreeNode('B')
# A.right = TreeNode('C')
# A.left.right = TreeNode('D')
A = 'A B # D # # C # #'

ans = deserialize(A)
print(ans)
