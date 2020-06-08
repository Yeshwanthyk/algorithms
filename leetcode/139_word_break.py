"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


def word_break(s, wordDict):

    n = len(s)
    res = [False] * (n + 1)
    res[0] = True

    for i in range(n):
        if res[i]:
            for w in wordDict:
                if i + len(w) <= n and s[i: i + len(w)] == w:
                    res[i + len(w)] = True

    return res[n]


s = "leetcode"
wordDict = ["leet", "code"]
ans = word_break(s, wordDict)
print(ans)
