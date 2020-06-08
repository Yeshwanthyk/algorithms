# DFS(Graph G, starting vertex s)
# if s is not visited, we set it to "visited"
# for every edge of (s,v):
# DFS(G,v)


def DFS(matrix):

    # Check to see if the matrix is empty
    if not matrix:
        return []

    visited = set()
    rows, cols = len(matrix), len(matrix[0])

    # We set the directions that the pointer can move in
    # We use this later to explore different directions
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):

        # We check to see if current coord is in visited
        if (i, j) in visited:
            return

        # If not, add it
        visited.add((i, j))

        # Explore in all directions recursively
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # logic for the problem is needed
                traverse(next_i, next_j)

    for i in range(rows):
        for i in range(cols):
            traverse(i, j)


"""
Given empty array, walk through and produce dfs
"""


# class Node:
#     def __init__(self, name):
#         self.childern = []
#         self.name = name

#     def add_child(self, name):
#         self.childern.append(Node(name))
#         return self

#     def depth_first_search(self, array):
#         array.append(self.name)

#         for childern in self.childern:
#             childern.depth_first_search(array)

# return array
