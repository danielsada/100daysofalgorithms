
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class UnorderedPriorityQueue:
    """"
    A little Unordered pq, the problem is that it takes linear time to get the max.
    """

    def __init__(self, tupled=False):
        self.queue = []
        self.tupled = tupled

    def insert(self, elem):
        self.queue.append(elem)

    def popMax(self):
        pass
        # if self.tupled:
        #     pass
        # else:
        #     maxi: int = 0
        #     for i, v in enumerate(self.queue):
        #         if maxi < i:
        #             maxi = i
        #     swap(maxi, N-1)
        #     return self.

    def swap(self, i, j):
        self.queue[i] ^= self.queue[j]
        self.queue[j] ^= self.queue[i]
        self.queue[i] ^= self.queue[j]
