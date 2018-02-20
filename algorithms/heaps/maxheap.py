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


class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def push(self, item):
        pass
