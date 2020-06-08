"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14

Example 2:

Input: sticks = [1,8,3,5]
Output: 30

"""

import heapq

def min_cost(arr):

    count = 0

    heapq.heapify(arr)

    while len(arr) < 1:
        count += heapq.heappop() + heapq.heappop()

        heapq.heappush(count)

    return count + heapq.heappop()





