def min_depth(T):
    if T is None:
        return 0

    # The conditions below cover the only edge case: when the root node has only
    # 1 child.
    if T.left is None:
        return 1 + min_depth(T.right)

    if T.right is None:
        return 1 + min_depth(T.left)

    return 1 + min(min_depth(T.left), min_depth(T.right))

def max_depth(T):
    if T is None:
        return 0

    return 1 + max(max_depth(T.left), max_depth(T.right))

def is_balanced(T):
    return max_depth(T) - min_depth(T) <= 1

def is_mirror(p, q):
    if p is None or q is None:
        return p == q

    return p.value == q.value and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

def lca(T, p, q):
    if T is None:
        return None

    # This is the LCA
    if T.value == p or T.value == q:
        return T

    # Explore subtrees.
    left_lca = lca(T.left, p, q)
    right_lca = lca(T.right, p, q)

    if left_lca and right_lca:
        return T

    return left_lca if left_lca is not None else right_lca

def lca_bst(T, p, q):
  if T is None:
    return None

  # Explore left subtree
  if T.value > p and T.value > q:
    return lca_bst(T.left, p, q)

  # Explore right subtree
  if T.value < p and T.value < q:
    return lca_bst(T.right, p, q)

  return T
