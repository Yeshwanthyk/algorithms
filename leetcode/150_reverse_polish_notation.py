"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

# Psuedocode
# ----------
# 1) Iterate through the list and add items to stack
# 2) If we come across +, -, /, * we evaluate last two digits
# 3) Keep moving through until stack is empty
# 4) Output result
import math


def eval_RPN(tokens):

    stack = []

    valid_operators = ("-", "+", "/", "*")

    for token in tokens:

        if token not in valid_operators:
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()

            # computed_var = (eval(str(var2) + token + str(var1)))
            if token == "+":
                computed_var = left + right
            elif token == "-":
                computed_var = left - right
            elif token == "*":
                computed_var = left * right
            else:
                computed_var = left / right

                if computed_var > 0:
                    computed_var = math.floor(computed_var)
                else:
                    computed_var = math.ceil(computed_var)

            stack.append(computed_var)

    return stack.pop()


tokens = ["4", "13", "5", "/", "+"]
ans = (eval_RPN(tokens))
print(ans)
