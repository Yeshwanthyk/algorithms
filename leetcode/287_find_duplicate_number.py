"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.
"""


def find_dupe(nums):

    if len(nums) < 1:
        return -1

    slow = nums[0]
    fast = nums[nums[0]]

    # we move the fast pointer twice that of slow pointer
    # once there meet, we know that there is cycle
    while (slow != fast):

        slow = nums[slow]
        fast = nums[nums[fast]]

    # Once they meet we use floyd's cycle algo to move both fast and slow one at a time
    # and the place they finally meet is the start of loop
    fast = 0
    while (fast != slow):
        slow = nums[slow]
        fast = nums[fast]

    return fast
