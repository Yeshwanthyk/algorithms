"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
import heapq


def meeting_room(intervals):

    if len(intervals) < 1:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    heap = []

    for interval in intervals:

        start_time = interval[0]
        end_time = interval[1]

        if not heap:
            heapq.heappush(heap, end_time)
        elif heap[0] > start_time:
            heapq.heappush(heap, end_time)
        else:
            heapq.heapreplace(heap, end_time)

    return len(heap)


intervals = [[7, 10], [2, 4]]
ans = meeting_room(intervals)
print(ans)
