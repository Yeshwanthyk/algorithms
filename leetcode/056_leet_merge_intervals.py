"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
import unittest


def merge_intervals(intervals):

    if len(intervals) < 1:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    m = []
    l, r = 0, 0

    for interval in sorted_intervals:
        if not m:
            m = [interval]
        else:
            l = m[-1:][0][0]
            r = m[-1:][0][1]

            if interval[0] <= r:
                r = max(r, interval[1])
                m.pop()
                m.append([l, r])
            else:
                m.append(interval)
    return m


intervals = [[1, 1], [2, 6], [8, 10], [1, 18]]
# intervals = [[]]
ans = merge_intervals(intervals)
print(ans)


def has_overlap(a, b):
    if a[1] >= b[0] and b[1] > a[0]:
        return True


def merge_overlapped(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]


def merge_intervals_v2(arr):

    ans = [arr[0]]
    for index in range(1, len(arr)):

        if not ans:
            ans.append(arr[index])

        if has_overlap(ans[-1], arr[index]):
            merged = merge_overlapped(ans[-1], arr[index])
            ans.pop()
            ans.append(merged)
        else:
            ans.append(arr[index])

    return ans


# class TestMergeIntervals(unittest.Testcase):
#     def test_merge_interval_works():
#         intervals = [[1, 4], [4, 5]]
#         self.assert(merge_intervals(intervals), [[1, 5]])


# if __name__ == '__main__':
#     unittest.main()
