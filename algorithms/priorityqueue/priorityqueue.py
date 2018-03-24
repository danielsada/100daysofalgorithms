from algorithms.heaps.maxheap import MaxHeap
from algorithms.heaps.minheap import MinHeap


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class PriorityQueue:
    """"
    A priority queue made with a max heap. It is performant.
    This is a proxy for a MaxHeap
    """

    def __init__(self, mx=True):
        if mx:
            self.pq: MaxHeap = MaxHeap()
        else:
            self.pq: MinHeap = MinHeap()

    def __len__(self):
        return len(self.pq)

    def __repr__(self):
        return f"PQ => {self.pq.elements} with peek {self.pq.peek()}"

    def add(self, elem):
        self.pq.push(elem)

    def pop(self):
        return self.pq.pop()

    def peek(self):
        return self.pq.peek()
