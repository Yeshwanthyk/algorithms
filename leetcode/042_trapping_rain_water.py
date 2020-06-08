"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


def trapping_rain_water(arr):

    left = 0
    right = len(arr) - 1

    max_left = 0
    max_right = 0
    ans = 0

    while left < right:

        if arr[left] < arr[right]:
            if arr[left] > max_left:
                max_left = arr[left]
            else:
                ans += max_left - arr[left]
            left += 1
        else:
            if arr[right] > max_right:
                max_right = arr[right]
            else:
                ans += max_right - arr[right]
            right -= 1

    return ans


array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = trapping_rain_water(array)
print(ans)
