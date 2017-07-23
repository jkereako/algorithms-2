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

def max_path_sum(T, path_sum=0):
    if T is None:
        return 0

    left_sum = max_path_sum(T.left)
    right_sum = max_path_sum(T.right)

    path_sum = max(path_sum, left_sum + right_sum + T.value)

    return max(left_sum, right_sum) + T.value

def has_path_sum(T, path_sum):
    """
    Recursively subtracts the tree node's value from the argument `path_sum`. If we
    have reached a leaf node and if `path_sum` reaches zero, then there exists a path
    which equals `path_sum`.
    """

    # If the current node, `T`, is a leaf and `sum` is 0
    if T is None:
        return path_sum == 0

    result = 0
    subtree_sum = path_sum - T.value

    # If both descendants of the current node, `T`, are leaves and `sum` is 0
    if subtree_sum == 0 and T.left == None and T.right == None:
        return True

    if T.left:
        result = result or has_path_sum(T.left, subtree_sum)

    if T.right:
        result = result or has_path_sum(T.right, subtree_sum)

    return result
