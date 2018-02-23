from algorithms.ugraph import UGraph
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class DepthFirstPaths:
    """"
    This is a Depth First Search.
    Finds a path between start s, and all other indexes. 
    Then query it to see if there is a path between two nodes.
    """

    def __init__(self, g: UGraph, s: int):
        self.marked: List[bool] = [False]*g.V
        self.edgeTo: List[int] = [None]*g.V
        self.s = s
        self.dfs(g, s)

    def dfs(self, g: UGraph, v: int):
        self.marked[v] = True
        for node in g.close(v):
            if not self.marked[node]:
                self.edgeTo[node] = v
                self.dfs(g, node)

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
