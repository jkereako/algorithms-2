def quicksort(L):
    """
    Developed in 1959 by Tony Hoare, quicksort is still a commonly used
    algorithm.

    Performance
    ===========
    Worst:      O(n^2)
    Average:    O(n log n)
    Best:       O(n log n)

    Space
    =====
    Worst:      O(n)
    Average:    O(n log n)
    """

    if len(L) <= 1:
        return L

    lesser = []
    greater = []
    pivots = []

    pivot = L[0]

    for val in L:
        if val < pivot:
            lesser.append(val)
        elif val > pivot:
            greater.append(val)
        else:
            pivots.append(val)

    lesser = sort(lesser)
    greater = sort(greater)

    return lesser + pivots + greater

def insertion_sort(L):
    """
    Insertion sort is a simple algorithm which builds the final sorted list 1
    item at a time.

    It compares the current element with it's neighbor to the left. If the
    current element is smaller than the neighbor, it then compares with the
    neighbor before that and so on until the beginning of the list is reached.

    Performance
    ===========
    Worst:      O(n^2)
    Average:    O(n^2)
    Best:       O(n)

    Space
    =====
    Worst:      O(1)
    """

    # Start from the second element so we can compare the current element with
    # the previous element.
    for i in range(1, len(L)):
        val = L[i]
        k = i

        # Start from the current position of the array and iterate backwards
        # toward the beginning of the array comparing adjascent values as you
        # go.
        while k > 0 and val < L[k - 1]:
            L[k] = L[k - 1]
            k -= 1

        L[k] = val

    return L

def selection_sort(L):
    """
    Selection sort is an in-place comparison sort. The algorithm divides the
    input list into 2 parts: the sublist of items already sorted, which is built
    from the front of the list toward the tail, and the sublist of items yet to
    be sorted. See the example below:

    [64, 25, 12, 22, 11]    # Initial state
    [11, 25, 12, 22, 64]    # sorted sublist = [11]
    [11, 12, 25, 22, 64]    # sorted sublist = [11, 12]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22, 25]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22, 25, 64]

    Performance
    ===========
    Worst:	    О(n^2)
    Average:    О(n^2)
    Best:       О(n^2)

    Space
    ===========
    Worst:      О(n) total, O(1) auxiliary
    """

    for i in range(len(L) - 1):
        #Invariant: L[:i] is sorted
        min_idx = i
        min_val= L[i]
        j = i + 1

        while j < len(L):
            if min_val > L[j]:
                min_idx = j
                min_val= L[j]
            j += 1

        temp = L[i]
        L[i] = L[min_idx]
        L[min_idx] = temp

def merge_sort(L, compare = lambda x, y: x < y):
    """
    Mergesort is a famous example of a divide and conquer algorithm invented in
    1945. It divides a list into 2 parts, sorts each part individually and then
    merges the 2 lists.

    Performance
    ===========
    Worst:      O(n log n)
    Avereage:   O(n log n)
    Best:       O(n log n)
    """

    # If L is fewer than 2 elements, then return a copy of the list
    if len(L) < 2:
        return list(L)

    # Divide and conquer!
    mid = len(L) // 2
    left = sort(L[:mid], compare)
    right = sort(L[mid:], compare)

    return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i,j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result


def sort(A):
    heapify(A)
    end = len(A) - 1

    while end > 0:
        A[end], A[0] = A[0], A[end]
        sift_down(A, 0, end - 1)
        end -= 1

    return A

def heapify(A):
    start = (len(A) - 2) // 2
    while start >= 0:
        sift_down(A, start, len(A) - 1)
        start -= 1

def sift_down(A, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and A[child] < A[child + 1]:
            child += 1
        if child <= end and A[root] < A[child]:
            A[root], A[child] = A[child], A[root]
            root = child
        else:
            return
