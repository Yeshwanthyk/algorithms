from collections import deque

def BFS(matrix):

    if not matrix:
        return []

    visited = set()
    rows, cols = len(matrix), len(matrix[0])
    directions = ((1,0), (-1,0), (0,1), (0,-1))

    def traverse(i,j):
        # this won't work. we will get each element; i and j, returned seperately
        # queue = deque((i,j))

        queue = deque([(i,j)])

        while queue:
            if (i,j) not in visited:
                visited.add((i,j))

                for direction in directions:
                    next_i, next_j = i + direction[0], j + direction[1]

                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        #logic
                        queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i,j)
