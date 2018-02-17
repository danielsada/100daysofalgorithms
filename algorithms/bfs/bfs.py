from algorithms.ugraph import UGraph
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BreadthFirstPaths:
    """"
    This is a Breadth First Search.
    This will also calculate the distances 
    between the nodes preemptively.
    Finds a path between start s, and all other indexes. 
    Then query it to see if there is a path between two nodes.
    """

    def __init__(self, g: UGraph, s: int):
        self.queue = []
        self.visited = [False] * g.num_V()
        self.distanceTo = [False] * g.num_V()
        self.edgeTo = [None] * g.num_V()
        self.g = g

        self.visited[s] = True
        self.queue.append(s)
        while len(self.queue) != 0:
            current_item = self.queue.pop()
            for elem in self.g.close(current_item):
                if not self.visited[elem]:
                    self.queue.insert(0, elem)
                    self.visited[elem] = True
                    self.edgeTo[elem] = current_item


# 72
