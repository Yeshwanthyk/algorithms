"""
"""


def minesweeper(grid, point):

    row = len(grid)
    col = len(grid[0])

    x = point[0]
    y = point[1]

    if grid[x][y] == M:
        grid[x][y] = "X"
        return grid

    dfs(grid, x, y)

    return grid


def dfs(grid, x, y):

    m, n = len(board), len(board[0])
    directions = [(-1, -1), (0, -1), (1, -1), (1, 0),
                  (1, 1), (0, 1), (-1, 1), (-1, 0)]

    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 'E':
        return

    mine_count = 0
    # check for mines
    for dir in directions:
        if grid[x+dir[0]][y+dir[1]] == 'M':
            mine_count += 1

    if mine_count:
        grid[x][y] = mine_count
    else:
        grid[x][y] = 'B'

    for dir in directions:
        dfs(grid, x + dir[0], y + dir[1])
