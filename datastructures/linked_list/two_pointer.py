class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


"""
876: Middle of linked list
"""


def find_median(LinkedList):

    slow = fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

    return slow.val


"""
141: Linked List Cycle
"""


def cycle_detection(LinkedList):

    slow = fast = head

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


"""
142: Linked List II
271: Find duplicate number

x ------ y --- z
        |     |
        |-----|

Ds - slow pointer
Dy - fast pointer travels 2x faster than Ds

Ds = x + y
Dy = x + y + z + y = x + 2y + z
2*Ds = Dy
2x + 2y = x + 2y + z
x = z

so to find start of the cycle we can reset fast = head
and move fast and slow one step until they meet. That would be the
start of the cycle
"""


def find_node_cycle_starts(LinkedList):

    slow = fast = head
    has_cycle = False

    # check if there is cycle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            has_cycle = True

    # reset fast pointer to head and move slow and fast by one step
    # where they meet is the start of the cycle
    if has_cycle:
        fast = head
        while fast and slow != fast:
            fast = fast.next
            slow = slow.next

        return slow

    return False


def remove_cycle_in_linked_list(LinkedList)

 slow = fast = head
  has_cycle = False

   # check if there is cycle
   while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            has_cycle = True

    # reset fast pointer to head and move slow and fast by one step
    # where they meet is the start of the cycle
    if has_cycle:
        fast = head
        # Stop a node before and reset the next pointer of that node to None
        while fast and slow.next != fast.next:
            fast = fast.next
            slow = slow.next

        slow = slow.next

    return False
