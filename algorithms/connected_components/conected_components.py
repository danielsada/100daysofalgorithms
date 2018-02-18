from algorithms.ugraph import UGraph
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class ConnectedComponents:
    """"
    This is a connected components class. 
    Given graph G, it tries to identify which groups of
    graphs there is. If you want a simple example, see the
    wand tool in photoshop.
    """

    def __init__(self, g: UGraph):
        self.id = [None]*g.V()
        self.marked = [False]*g.V()
        self.curr_component = 0
        self.num_of_components = 0
        for elem in range(0, g.V()):
            if not self.marked[elem]:
                self.dfs(g, elem)
                self.curr_component += 1

    def count(self):
        return self.num_of_components

    def ID(self, v: int):
        return self.id[v]

    def dfs(self, g: UGraph, v: int):
        self.marked[v] = True
        self.id[v] = self.curr_component
        for node in g.close(v):
            if not self.marked[node]:
                self.dfs(g, node)
