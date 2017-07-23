
def lca(T, v, w):
    """
    The lowest common ancestor (LCA) of two nodes v and w in a tree or directed
    acyclic graph (DAG) T is the lowest (i.e. deepest) node that has both v and
    w as descendants, where we define each node to be a descendant of itself
    (so if v has a direct connection from w, w is the lowest common ancestor).
    """
    if T is None:
        return None

    # This is the LCA
    if T.value == v or T.value == w:
        return T

    # Explore subtrees.
    left_lca = lca(T.left, v, w)
    right_lca = lca(T.right, v, w)

    if left_lca and right_lca:
        return T

    return left_lca if left_lca is not None else right_lca

def lca_bst(T, v, w):
  if T is None:
    return None

  # Explore left subtree
  if T.value > v and T.value > w:
    return lca_bst(T.left, p, q)

  # Explore right subtree
  if T.value < v and T.value < w:
    return lca_bst(T.right, p, q)

  return T
