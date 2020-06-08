"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


def decode_string(s):

    if not s:
        return s

    stack = []

    for i in s:

        if i == "[":
            stack.append(i)
            continue

        stack.append(i)

        if i == ']':
            # remove `]` that gets pushed into the stack
            popped = stack.pop()
            str = ""
            dig = 0

            while True:

                # concat the string until we hit `[`
                while popped != '[' and stack:
                    str = stack.pop() + str
                else:
                    break

                if popped == '[':
                    stack.pop()

                    while True:
                        if not stack or not stack[-1].isdigit():
                            break
                        else:
                            dig = stack.pop() + dig
                    str = int(dig) * str
                    break

    return ''.join(stack)


s = "2[20[xy]]pq"
ans = decode_string(s)
print(ans)
