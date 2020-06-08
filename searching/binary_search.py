import unittest


def binary_search(array, val):

    lo, hi = 0, len(array) - 1

    while (lo <= hi):

        mid = lo + (hi - lo) // 2

        if array[mid][1] == val:
            return mid

        if array[mid][1] < val:
            lo = mid + 1
        else:
            hi = mid - 1

    if array[mid][1] < val or mid == 0:
        return array[mid]
    else:
        return array[mid-1]


def binary_search_recursive(array, val, lo, hi):

    if lo > hi:
        return None

    mid = (hi - lo)//2 + lo

    if array[mid] == val:
        return mid
    elif array[mid] > val:
        return binary_search_recursive(array, val, lo, mid - 1)
    else:
        return binary_search_recursive(array, val, mid + 1, hi)


# array = [[1, 100], [4, 150], [3, 180], [6, 220]]
# ans = binary_search(array, 170)
# print(ans)

class TestBinarySearch(unittest.TestCase):

    def test_if_we_get_back_correct_answer_for_valid_list(self):
        array = [[1, 100], [4, 150], [3, 180], [6, 220]]
        ans = binary_search(array, 150)
        self.assertEqual(ans, 1)


if __name__ == '__main__':
    unittest.main()
