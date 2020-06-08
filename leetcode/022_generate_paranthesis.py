"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

import unittest


def generate_parentheses(num):

    if not num:
        return

    left, right = num, num
    res = []

    dfs(left, right, res, "")
    return res


def dfs(left, right, res, end_string):

    if right < left:
        return

    if not left and not right:
        res.append(end_string)
        return

    if left:
        dfs(left - 1, right, res, end_string + "(")

    if right:
        dfs(left, right - 1, res, end_string + ")")


class TestGenerateParentheses(unittest.TestCase):

    def test_params_works_correctly(self):

        n = 3
        expected = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]

        ans = generate_parentheses(n)
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
