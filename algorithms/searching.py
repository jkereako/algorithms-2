def binary_search(L, key):
    """
    Binary search, or half-interval search, finds the position of a target value
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

def bfs_connected_components(G, source):
  visited = []
  queue = [source]

  while queue:
    # Visit oldest vertex first
    vertex = queue.pop(0)

    if vertex not in visited:
      visited.append(vertex)
      queue.extend(G[vertex])

  return visited

def bfs_paths(G, source, destination):
  queue = [source] # Visit oldest vertex first
  source_paths = [[source]] # Keeps track of all paths originating from the source
  valid_paths = [] # Valid paths from the source to the destination

  while queue:
    vertex = queue.pop(0)
    visited = source_paths.pop(0)

    # Visit adjacent vertices
    for adjacent_vertex in G[vertex]:
      if adjacent_vertex in visited:
        continue

      path = visited + [adjacent_vertex]

      if adjacent_vertex == destination:
        valid_paths.append(path)

      else:
        source_paths.append(path)
        queue.append(adjacent_vertex)

  return valid_paths

def dfs_connected_components(G, source):
  visited = []
  stack = [source]

  while stack:
    # Visit newest vertex first
    vertex = stack.pop()

    if vertex not in visited:
      visited.append(vertex)
      stack.extend(G[vertex])

  return visited

def dfs_paths(G, source, destination):
  stack = [source] # Visit newest vertex first
  source_paths = [[source]] # Keeps track of all paths originating from the source
  valid_paths = [] # Valid paths from the source to the destination

  while stack:
    vertex = stack.pop()
    visited = source_paths.pop()

    # Visit adjacent vertices
    for adjacent_vertex in G[vertex]:
      if adjacent_vertex in visited:
        continue

      path = visited + [adjacent_vertex]

      if adjacent_vertex == destination:
        valid_paths.append(path)

      else:
        source_paths.append(path)
        stack.append(adjacent_vertex)

  return valid_paths
