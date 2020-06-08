"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


"""
import unittest


def find_elem(arr, target):

    lo = 0
    hi = len(arr)

    start_index = -1
    end_index = -1

    while lo <= hi:

        mid = (hi - lo) // 2

        if arr[mid] == target:
            start_index = mid
            end_index = mid
            break

        if target > mid:
            hi = mid - 1
        else:
            lo = mid + 1

    while arr[end_index+1] == target:
        end_index += 1

    return [start_index, end_index]


class TestFindElem(unittest.TestCase):

    def test_get_indexes_for_valid_arr(self):

        arr = [5, 7, 7, 8, 8, 10]

        expected = [3, 4]
        actual = find_elem(arr, 8)

        self.assertEquals(expected, actual)

    def test_get_indexes_for_valid_arr_single(self):

        arr = [5, 7, 7, 8, 9, 10]

        expected = [3, 3]
        actual = find_elem(arr, 8)

        self.assertEquals(expected, actual)

    def test_get_indexes_for_valid_arr_unfound_target(self):

        arr = [5, 7, 7, 8, 9, 10]

        expected = [-1, -1]
        actual = find_elem(arr, 4)

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
    # arr = [5, 7, 7, 8, 9, 10]
    # ans = find_elem(arr, 4)
    # print(ans)
