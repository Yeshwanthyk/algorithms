"""
You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""


from collections import deque


def walls_and_gates(arr):

    row, col = len(arr), len(arr[0])

    for i in range(row):
        for jj in range(col):
            if arr[i][jj] == 0:
                traverse(arr, i, jj, 0)

    return arr


def traverse(arr, i, jj, dist):

    if 0 > i or i >= len(arr) or 0 > jj or jj >= len(arr[0]) or arr[i][jj] < dist:
        return

    arr[i][jj] = dist

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dir in directions:
        traverse(arr, i + dir[0], jj + dir[1], dist + 1)


def walls_bfs(arr):

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse_bfs(row, col):
        queue = deque((row, col, 1))

        while queue:
            x, y, val = queue.popleft()

            if x < 0 or x >= len(arr) or y < 0 or y >= len(arr) or rooms[x][y] <= val:
                continue

            arr[x][y] = val

            for dir in directions:
                queue.extend(x + dir[0], y + dir[1], val + 1)

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 0:
                traverse_bfs(row, col)

    return arr


arr = [[1000, -1, 0, 1000], [1000, 1000, 1000, -1],
       [1000, -1, 1000, -1], [0, -1, 1000, 1000]]

ans = walls_and_gates(arr)
print(ans)
