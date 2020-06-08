"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def move_zeroes(nums):

    slow = fast = 0

    while fast < len(nums):

        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # we wait to find a zero to slow when moving the slow pointer
        if nums[slow] != 0:
            slow += 1

        fast += 1

    return nums


nums = [0, 1, 0, 3, 12]
ans = move_zeroes(nums)
print(ans)
