"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from collections import defaultdict, deque


def word_ladder(beginWord, endWord, wordList):

    dic = defaultdict(list)

    for w in wordList:
        for i in range(len(w)):
            s = w[:i] + "_" + w[i+1:]
            dic[s] = [w]

    return bfs(dic, beginWord, endWord)


def bfs(dic, beginWord, endWord):

    steps = 0

    queue, visited = deque([(beginWord, 1)]), set()

    while queue:
        word, steps = queue.popleft()

        if word not in visited:

            if word == endWord:
                return steps

            visited.add(word)

            for i in range(len(word)):

                sw = word[:i] + "_" + word[i+1:]

                if sw in dic:
                    # If we find the next iteration we add the word to the queue
                    if dic[sw][0] not in visited:
                        queue.extend([(dic[sw][0], steps + 1)])
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

ans = word_ladder(beginWord, endWord, wordList)
print(ans)
