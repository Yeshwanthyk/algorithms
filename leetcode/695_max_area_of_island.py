"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.

"""


def max_area_island(grid):

    max_area = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                area = [0]
                traverse(grid, area, row, col)
                max_area = max(max_area, area[0])

    return max_area


def traverse(grid, area, row, col):

    if not (0 <= row < len(grid) and 0 <= col < len(grid)) or grid[row][col] != 1:
        return

    area[0] += 1
    grid[row][col] = '#'

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dir in dirs:
        traverse(grid, area, row + dir[0], col + dir[1])


grid = [[0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
ans = max_area_island(grid)
print(ans)
