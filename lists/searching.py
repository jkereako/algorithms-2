def recursive_linear_search(L, x, inc=0):
  # We've reached the end of the list
  if len(L) - 1 < inc:
    return None

  if L[inc] == x:
    return inc

  # Inspect the next element
  return recursive_linear_search(L, x, inc + 1)

def binary_search(L, key):
    """
    Binary search, also known as half-interval search, logarithmic search or
    binary chop is a search algorithm that finds the position of a target value
    within a sorted array.

    Performance
    ===========
    Worst:      O(log n)
    Average:    O(log n)
    Best:       O(1)

    Space
    =====
    Worst:      O(1)
    """

    # The list is empty, hence, the key does not exist.
    if len(L) == 0:
        return False

    # The list only contains 1 element, test if it is the key
    if len(L) == 1:
        return L[0] == key

    # Find the middle key
    mid = len(L) // 2

    # We found the key
    if L[mid] == key:
        return True

    # If the middle element is greater than the key, then search the lower
    # half of L.
    if L[mid] > key:
        return binary_search(L[:mid], key)

    # Otherwise, search the upper half
    return binary_search(L[mid:], key)

def max_subarray(L):
    """
    Also known as Kadane's algorithm, this problem was first posed by Ulf
    Grenander of Brown University in 1977. A linear time algorithm was found
    soon afterwards by Jay Kadane of Carnegie Mellon University.

    Performance
    ===========
    O(n)
    """
    max_ending_here = max_so_far = L[0]

    for x in L[1:]:
        # `max_ending_here` keeps a running total of the maximum subarray.
        max_ending_here = max(x, max_ending_here + x)

        # `max_so_far` changes only twice; once at the beginning of the maximum
        # subarray and once at the end.
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
