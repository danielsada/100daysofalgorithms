from algorithms.digraph.digraph import DiGraph
from algorithms.dfs.topologicalsort import TopologicalSort

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class DirectedCC:
    """
    KosajaruSharir is an algorithm that allows us to detect
    strongly connected components.
    """

    def __init__(self, g: DiGraph):
        self.id = [None]*(g.V+1)
        self.marked = [False]*(g.V+1)
        self.curr_component = 0
        self.num_of_components = 0
        tsort = TopologicalSort(g.reverse())
        postorder = tsort.get_postorder()
        self.g = g
        for elem in postorder:
            if not self.marked[elem]:
                self.dfs(g, elem)
                self.curr_component += 1
                self.num_of_components += 1

    def count(self):
        return self.num_of_components

    def ID(self, v: int):
        return self.id[v]

    def dfs(self, g: DiGraph, v: int):
        self.marked[v] = True
        self.id[v] = self.curr_component
        for node in g.close(v):
            if not self.marked[node]:
                self.dfs(g, node)
