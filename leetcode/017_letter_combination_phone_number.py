"""

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


def phone(input):

    phone_dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl'
    }

    res = []

    def make_combinations(index, cur):

        if index == len(input):
            if len(cur) > 0:
                res.append(''.join(cur))
            return

        for ch in phone_dic[input[index]]:
            cur.append(ch)
            make_combinations(index+1, cur)
            cur.pop()

    make_combinations(0, [])
    return res


input = '234'
ans = phone(input)
print(ans)
