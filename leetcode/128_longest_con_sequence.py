"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


def longest_con_seq(arr):

    arr = set(arr)
    max_len = 0

    for num in arr:

        if not num - 1 in arr:

            y = num + 1

            while y in arr:
                y += 1

            max_len = max(max_len, y - num)

    return max_len


arr = [100, 4, 200, 1, 201, 5, 199, 3, 2]
ans = longest_con_seq(arr)
print(ans)
