"""Binary First Search"""

from algorithms.ugraph import UGraph

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
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.s = s
        self.g = g

        self.marked[s] = True
        self.queue.append(s)
        while self.queue:
            current_item = self.queue.pop(0)
            for elem in self.g.close(current_item):
                if not self.marked[elem]:
                    self.queue.insert(0, elem)
                    self.marked[elem] = True
                    self.edgeTo[elem] = current_item

    def hasPathTo(self, v: int):
        return self.marked[v]

    def pathTo(self, v: int):
        if not self.hasPathTo(v):
            return None
        path = []
        init = v
        while init != self.s:
            path.append(init)
            init = self.edgeTo[init]
        path.append(self.s)
        return path
