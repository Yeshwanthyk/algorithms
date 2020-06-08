"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


def group_anagrams(arr):

    dic = {}
    for w in arr:
        key = tuple(sorted(w))

        # using dict get
        # dic[key] = dic.get(key, []) + [w]
        if key in dic:
            dic[key].append(w)
        else:
            dic[key] = [w]

    return list(dic.values())


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = group_anagrams(arr)
print(ans)
