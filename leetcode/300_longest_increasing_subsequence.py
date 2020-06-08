"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""
import unittest


def LCS(array):

    # ! Forgot edge cases
    if not array:
        return 0

    if len(array) == 1:
        return 1

    i, j = 0, 1

    ret = [1 for x in range(len(array))]

    while j < len(array):
        sub = 1

        for i in range(j+1):

            # ! Forgot to add in equality check. Its longest INCREASING subsequence.
            if array[i] >= array[j] or i == j:
                continue
            else:
                sub = max(sub, ret[i] + 1)

        ret[j] = sub
        j += 1

    return max(ret)


class TestLCS(unittest.TestCase):

    def test_getting_expected_output(self):

        array = [10, 9, 2, 5, 3, 7, 10]
        ans = LCS(array)
        self.assertEqual(ans, 4)


if __name__ == '__main__':
    unittest.main()
