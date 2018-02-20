import heapq

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
This isn't in the current pathway, but I wanted to take some 
time to make a MaxHeap in python.
Interesting note, is that the default heap implementation is
a min heap
"""


class Heap:
    def __init__(self):
        self.size = 0

    @staticmethod
    def left_index(parentIndex):
        return 2*parentIndex + 1

    @staticmethod
    def right_index(parentIndex):
        return 2*parentIndex + 2

    @staticmethod
    def has_right_index(parentIndex):
        pass


class MaxHeap:

    def __init__(self):
        self.sz = 0

    def exists_left(parentIndex):
        return

    def push(self, item):
        heapq.heappush(self.ls, item)
        print(self.ls)

    def pop(self):
        elem = heapq.nlargest(1, self.ls)
        print(elem[0])
        self.ls.remove(elem[0])
        heapq.heapify(self.ls)
        print(self.ls)
