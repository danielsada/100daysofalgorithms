from algorithms.heaps.heap import Heap

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
This isn't in the current pathway, but I wanted to take some 
time to make a MaxHeap in python.
Interesting note, is that the default heap implementation is
a min heap
"""


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def peek(self):
        if Heap.size <= 0:
            raise IndexError("Well, you went out of the bucket friend.")
        return Heap.elements[0]

    def push(self, item):
        Heap.elements.append(item)
        Heap.size += 1
        self.heapifyUp()

    def pop(self):
        if Heap.size <= 0:
            raise IndexError("Well, you went out of the bucket friend.")
        returnItem = Heap.elements[0]
        Heap.elements[0] = Heap.elements[Heap.size - 1]
        Heap.size -= 1
        self.heapifyDown()
        return returnItem

    def heapifyDown(self):
        pass

    def heapifyUp(self):
        pass


hs = MinHeap()
hs.push(3)
print(hs.peek())
