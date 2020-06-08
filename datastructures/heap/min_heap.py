class Node:

    def __init__(self, name, value):
        self.name = name
        self.val = val


class MinHeap:

    def __init__(self), array:
        self.heap_dict = {}
        self.heap = self.build_heap(array)

    def __getitem__(self, key):
        return self.heap_dict[key]

    def get_parent_idx(self, idx):
        return (idx + 1) // 2

    def get_left_child_idx(self, idx):
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        return idx * 2 + 2

    def build_heap(self, array):

        last_idx = len(array) - 1
        start_from = self.get_parent_idx(last_idx)

        for idx, i in enumerate(array):
            self.heap_dict[i.name] = i.val

        for idx in range(start_from, -1, -1):
            self.sift_down(idx, array)

    def sift_down(self, idx, array):

        while True:
            left_child = self.get_left_child_idx(start_from)
            right_child = self.get_right_child_idx(start_from)

            smallest = idx

            if left_child < len(array) and array[left_child] < array[idx]:
                smallest = left_child
            else right_child < len(array) and array[right_child] < array[idx]:
                smallest = right_child

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                idx = smallest
            else:
                break

    def sift_up(self, idx):
        parent = self.get_parent_idx(idx)

        while parent >= 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = self.get_parent_idx(idx)

    def remove(self):

        # We move the root node to the last position of the array so that it can be
        # popped and we still maintain the heap propety
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        self.heap.pop()

        # We run min-heapify to ensure the heap property is maintained
        self.sift_down(0, self.heap)

    def insert(self, node):
        self.heap.append(node)
        self.sift_up(len(self.heap) - 1)
