"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is 
surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1

    Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3

"""


def number_of_islands(matrix):

    if not matrix:
        return 0

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                traverse(matrix, i, j)
                count += 1
    return count


def traverse(matrix, i, j):

    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
        return
    matrix[i][j] = '#'
    # traverse(grid, i+1, j)
    # traverse(grid, i-1, j)
    # traverse(grid, i, j+1)
    # traverse(grid, i, j-1)
    # if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != '1':
    #     return

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dir in directions:
        next_i, next_j = i + dir[0], j + dir[1]
        traverse(matrix, next_i, next_j)
    # traverse(matrix, i, j+1)
    # traverse(matrix, i, j-1)
    # traverse(matrix, i+1, j)
    # traverse(matrix, i-1, j)


matrix = [["1", "1", "0", "1", "0"], ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
ans = number_of_islands(matrix)
print(ans)
