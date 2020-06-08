def lca(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root


def LCA_bst(root, p, q):

    if not root:
        return

    if not p or not q:
        return

    if p < root.val and q < root.val:
        return LCA_bst(root.left)

    if p > root.val and q > root.val:
        return LCA_bst(root.right)

    if p == root.val:
        return p

    if q == root.val:
        return q

    return root
