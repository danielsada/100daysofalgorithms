from algorithms.heaps.heap import Heap

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
This isn't in the current pathway, but I wanted to take some
time to make a Heap in python.
Interesting note, is that the default heap implementation is
a min heap
"""


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def peek(self):
        if self.size <= 0:
            raise IndexError("Well, you went out of the bucket friend.")
        return self.elements[0]

    def push(self, item):
        self.elements.append(item)
        self.heapifyUp()

    def pop(self):
        if self.size <= 0:
            raise IndexError("Well, you went out of the bucket friend.")
        item = self.elements[0]
        self.elements[0] = self.elements[-1]
        del self.elements[-1]
        self.heapifyDown(item)
        return item

    def heapifyDown(self, val):
        index = 0
        while self.has_left_index(index):
            largeValueIndex = self.left_index(index)
            if self.has_right_index(index) and self.value_right(index) > self.value_left(index):
                largeValueIndex = self.right_index(index)
            if self.elements[index] > self.elements[largeValueIndex]:
                break
            else:
                self.swap(index, largeValueIndex)
            index = largeValueIndex

    def heapifyUp(self):
        last_element = self.size - 1
        while self.has_parent(last_element) and self.value_parent(last_element) < self.elements[last_element]:
            self.swap(self.parent_index(last_element), last_element)
            last_element = self.parent_index(last_element)
