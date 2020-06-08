"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

 

Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].
"""

import heapq
from collections import Counter


def task_scheduler(arr, n):

    # if cooling number is 2, then the difference between two same items must be n + 1
    n += 1

    ans = 0

    dic = Counter(arr)

    min_heap = [-v for v in dic.values()]
    heapq.heapify(min_heap)

    while min_heap:

        cnt = 0
        stack = []

        for _ in range(n):
            if min_heap:
                top = heapq.heappop(min_heap)
                cnt += 1

                if top < -1:
                    stack.append(top + 1)

        for i in stack:
            heapq.heappush(min_heap, i)

        if min_heap:
            ans += n
        else:
            ans += cnt

    return ans


arr = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2

ans = task_scheduler(arr, n)
print(ans)
