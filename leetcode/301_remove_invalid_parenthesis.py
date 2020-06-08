"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]

Example 4:
Input: "()))((()))"
Output: "()()"
"""
















def remove_invalid_paren(input):

    if input == "":
        return [""]

    result = []
    visited = set()

    left, right = 0, 0

    # Find extra paren
    for i in input:
        if i == "(":
            left += 1

        if i == ")":

            if left > 0:
                left -= 1
            else:
                right += 1

    dfs(input, 0, result, visited, left, right)
    return result


def DFS(s, index, result, visited, left, right):

    # Base case to append the final string
    visited.add(s)

    if left == 0 and right == 0:
        if is_valid(s):
            result.append(s)

    for i in range(index, len(s)):

        if s[i] != "(" and s[i] != ")":
            continue

        if s[i] == "(" and left == 0:
            continue

        if s[i] == ")" and right == 0:
            continue

        nxt = s[:i] + s[i+1:]
        if nxt not in visited:
            DFS(nxt, i, result, visited, left -
                (s[i] == "("), right - (s[i] == ")"))


def is_valid(s):
    for i in s:
        if i == "(":
            left += 1

        if i == ")":

            if left > 0:
                left -= 1
            else:
                right += 1

    if left == 0 and right == 0:
        return True
    else:
        return False


s = "()())()"
ans = remove_invalid_paren(s)
