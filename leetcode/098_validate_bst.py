def valid_bst(root):

    stack = []
    prev = None

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev and root.val <= prev.val:
            return False

        prev = root
        root = root.right

    return True
