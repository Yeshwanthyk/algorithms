class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        newNode = Node(data)
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode

    def add_tail(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            tmp = self.head
            while (tmp.next is not None):
                tmp = tmp.next
            tmp = Node(data)

    def print_list(self):
        tmp = self.head
        print(tmp.data)
        while(tmp.next != None):
            tmp = tmp.next
            print(tmp.data)


l1 = LinkedList()
l1.add_head(3)
l1.add_head(7)
l1.add_head(4)
l1.add_head(9)
l1.add_tail(6)
l1.print_list()
