"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Check to see if the key exists
        # If it does, we need to remove it from the DLL
        # and add it to the tailend as it was recently used

        node = dic.get(key, -1)
        if node:
            remove(node)
            add(node)

        return node.val

    def put(self, key, value):
        # If the key exists we need to remove it from
        # the DLL
        if key in dict:
            self.remove(dict[key])

        # Add new node to DLL and dict
        n = Node(key, val)
        self.add(n)
        self.dic[key] = n

        # if capacity is exceeded, remove the least used variable DLL
        if len(dict) > self.capacity:
            least_used_node = self.head.next
            self.remove(least_used_node)
            del self.dic[key]

    def add(n):
        # Assign tmp with last element from tail
        tmp = self.tail.prev

        # Add tmp.next to new node
        tmp.next = n

        # Add tail prev to new node
        n.next = self.tail

        # Set new nodes prev and next
        n.prev = tmp
        self.tail.prev = n

    def remove(n):
        # We set the next and previous nodes to the current node
        # and assign them to each other
        p = n.prev
        n = n.next

        p.next = n
        n.prev = p
