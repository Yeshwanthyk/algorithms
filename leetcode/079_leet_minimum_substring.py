"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Similar template:
- Longest Substring with At Most Two Distinct Characters
-  Longest Substring Without Repeating Characters
"""

from collections import Counter

# Psuedo Code
# * Two pointer system - start, end
# * Move end to find all the characters of T in S
# * Retract start to find min_win
# * Keep moving `end` till S is over and keep updating min_win


def min_window(S, T):

    if not S:
        return ""

    start = 0

    # Make a hashmap of the string we need to find
    T_map = Counter(T)
    # Keep track of the number of chars of T we found in S
    T_len = len(T)

    min_win = ""

    for end, char in enumerate(S):

        # If we find a char from T in S, we reduce `T_len`. If `T_len` becomes 0 we know that we found all the
        # chars in T
        if T_map[char] > 0:
            T_len -= 1

        # We keep adding all the chars of S we move through to the hashmap
        # Later when we start retracting `start`, this would help us to ensure we retract correctly
        T_map[char] -= 1

        while (T_len == 0):

            # Find length of the current substring that contains all chars of `T`. Later on as we keep retracting
            # if we find a smaller substring we can update `min_win` with that
            min_len = end - start + 1

            # if min_win is empty or if the len of new window is lesser than the older substring, we update it
            if not min_win or min_len < len(min_win):
                min_win = S[start:end+1]

            # we update the first char, and we check if is a part of `T`. If it is, we move `end` until we
            # find another substring
            T_map[S[start]] += 1

            if (T_map[S[start]] > 0):
                T_len += 1

            start += 1

    return min_win


S = "ADOBECODEBANC"
T = "ABC"
ans = min_window(S, T)
print(ans)
