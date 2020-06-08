"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


def container(array):

    lo, hi = 0, len(array) - 1
    max_vol = 0

    while lo < hi:

        vol = (hi - lo) * min(array[lo], array[hi])

        if max_vol < vol:
            max_vol = vol

        if array[lo] < array[hi]:
            lo += 1
        else:
            hi -= 1

    return max_vol


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = container(array)
