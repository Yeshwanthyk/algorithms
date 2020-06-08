"""
https://github.com/liyin2015/Algorithms-and-Coding-Interviews/blob/master/tree_questions.pdf
"""


"""
110. Balanced Binary tree
"""


def is_balanced(root):

    def dfs(root):

        if root is None:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        if left == -2 or right == -2 or abs(left - right) > 1:
            return -2

        return 1 + max(left, right)

    return dfs(root) != -2


"""
543. Diameter of BT
"""


def diameter_bt(root):

    def dfs(root, ans):

        if root is None:
            return -1

        left = dfs(root.left, ans)
        right = dfs(root.right, ans)

        # left + right + 2 edges
        ans[0] = max(ans[0], left + right + 2)

        return max(left, right) + 1

    ans = [0]
    dfs(root, ans)


"""
PATH Problems

max/min of each path/ path sum/ path length to
                                1) root - left
                                2) root - any node
                                3) any node - any node

Usual techniques:
1) DFS + global variables + current path variables in parameters of rec call
to track path and collect results

2) DFS + divide and conquer. Get left, get right and merge results

"""

"""
112. Path Sum
"""


def path_sum(root, target):

    if not root:
        return False

    if not root.left or root.right:
        return True if target == root.val else False

    left = path_sum(root.left, target - root.val)

    if left:
        return True

    right = path_sum(root.right, target - root.val)

    if right:
        return True

    return False


"""
129. Sum root to leaf number
       1
  2        3
4   5

124 + 125 + 13 = 262
"""


def root_sum(root):

    digits = []

    dfs(root, "", digits)

    ans = 0

    for d in digits:
        ans += int(d)

    return d


def dfs(root, temp_str, digits):

    if not root:
        return

    temp_str += root.val
    if not root.left and not root.right:
        digits.append(temp_str)

    dfs(root.left, temp_str, digits)
    dfs(root.right, temp_str, digits)


"""
437. Path Sum III
Find number of paths that sum to given value

. The idea here in naive implementation would be to do DUAL RECURRENCE w/
divide and conquer

. Prefix Sum Optimizatio
"""


def root_to_any_node(root, target_sum):

    if root is None:
        return 0

    target_sum -= root.val

    count = 0

    if target_sum == 0:
        count += 1

    return count + root_to_any_node(root.left, target_sum) + root_to_any_node(root.right, target_sum)


def path_sum_3(root, target_sum):

    if root is None:
        return 0

    return root_to_any_node(root, target_sum) + path_sum_3(root.left, target_sum) + path_sum_3(root.right, target_sum)


"""
124. Binary Tree Max Sum

"""


def max_root_to_any(root):

    if root is None:
        return 0

    left = max_root_to_any(root.left)
    right = max_root_to_any(root.right)

    # If left and right or neg, we get rid of it
    return root.val + max(0, (left, right))


def max_sum(root):

    if root is None:
        return 0

    ans = 0

    helper(root, ans)
    return ans


def helper(root, ans):

    if root is None:
        return 0

    left = max_root_to_any(root.left)
    right = max_root_to_any(root.right)

    ans = max(ans, max(0, left) + max(0, right) + root.val)

    helper(root.left, ans)
    helper(root.right, ans)
    return


"""
617. Merge two BT
"""


def merge_bt(root1, root2):

    if not root1 and not root2:
        return None

    if not root1 and root2:
        return root2

    if root1 and not root2:
        return root1

    node = TreeNode(root1.val + root2.val)

    node.left = merge_bt(root1.left, root2.left)
    node.right = merge_bt(root1.right, root2.right)

    return node


"""
226. Invert BT
      4
  2       7 
1   3   6   9 


      4
  7       2
9   6   3   1 

"""


def invert_bt(root):

    if root is None:
        return

    node = TreeNode(root.val)

    node.left = invert_bt(root.right)
    node.right = invert_bt(root.left)

    return node


"""
654. Max BT

1) Root is max number in array
2) Left subtree max is max tree contructed from left array
3) Right "                                      right "


"""


def max_bt(arr):

    if not arr
    return

    m, i = max([(v, i) for i, v in enumerate(arr)])

    root = TreeNode(m)

    root.left = max_bt(arr[:i])
    root.right = max_bt(arr[i+1:])

    return root
