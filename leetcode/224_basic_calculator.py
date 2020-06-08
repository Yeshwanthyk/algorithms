"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


def basic_calc(input):

    stack = []
    result = 0
    sign = 1
    num = 0

    for s in input:

        if s.is_digit():
            num = 10*num + int(s)

        if s in ["-", "+"]:
            res += sign * num

            num = 0
            if s == "-":
                sign = -1
            else:
                sign = 1

        if s == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1

        if s == ")":
            res += sign * num
            res *= stack.pop()  # its the `sign` stored in stack when we came across '('

            res += stack.pop()

    return res + num * sign


input = "(1+(14-15 + 11) )"
