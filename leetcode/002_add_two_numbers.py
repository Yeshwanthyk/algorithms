"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Problems I missed:
- What if a carry is left over
- what if one of them has just 0 -- [1, 8][0]
- Added new bugs like if first val starts with 0
- Not carry over values correctly using `carry`
"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):

    if not l1 or (l1.val == 0 and l1.next is None):
        return l2
    if not l2 or (l2.val == 0 and l1.next is None):
        return l1

    carry = 0
    tmp = new_node = ListNode(0)

    while l1 or l2:

        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        if carry >= 10:
            tmp.next = ListNode(carry - 10)
            carry = 1
        else:
            tmp.next = ListNode(carry)
            carry = 0

        tmp = tmp.next

        if l1 is None and l2 is None and carry:
            tmp.next = ListNode(carry)

    return new_node.next


# [0,8,6,5,6,8,3,5,7]
# [6,7,8,0,8,5,8,9,7]

l1 = ListNode(0)
l1.next = ListNode(8)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(5)
l1.next.next.next = ListNode(6)
l1.next.next.next.next = ListNode(8)
l1.next.next.next.next.next = ListNode(3)
l1.next.next.next.next.next.next = ListNode(5)
l1.next.next.next.next.next.next.next = ListNode(7)

l2 = ListNode(6)
l2.next = ListNode(7)
l2.next.next = ListNode(8)
l2.next.next.next = ListNode(0)
l2.next.next.next = ListNode(8)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = ListNode(8)
l2.next.next.next.next.next.next = ListNode(9)
l2.next.next.next.next.next.next.next = ListNode(7)


ans = add_two_numbers(l1, l2)
breakpoint()
print(ans)
