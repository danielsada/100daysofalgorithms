from algorithms.heaps.maxheap import MaxHeap


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class PriorityQueue:
    """"
    A priority queue made with a max heap. It is performant.
    """

    def __init__(self, tupled=False):
        self.tupled = tupled
        self.pq: MaxHeap = MaxHeap()

    def add(self, elem):
        self.pq.push(elem)

    def pop(self):
        return self.pq.pop()

    def peek(self):
        return self.pq.peek()


