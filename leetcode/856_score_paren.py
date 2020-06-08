"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6

"""


def score(input):

    stack = [0]

    for ch in input:

        if ch == "(":
            stack.append(0)

        if ch == ")":

            top = stack.pop()

            if stack[-1]:
                stack[-1] += top * 2
            else:
                stack[-1] += 1

    return stack.pop()
