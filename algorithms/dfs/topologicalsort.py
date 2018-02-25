from algorithms.digraph.digraph import DiGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class TopologicalSort:
    """"
    This class orders by precedence, so that the precedence is respected.
    """

    def __init__(self, g):
        self.marked = [False] * g.V
        self.stack = []
        self.g = g
        for i in range(0, g.V):
            if not self.marked[i]:
                self.dfs(self.g, i)

    def dfs(self, g: DiGraph, i: int):
        self.marked[i] = True
        for nodes in g.close(i):
            if not self.marked[nodes]:
                self.dfs(g, i)
            self.stack.append(i)

    def get_order(self):
        return self.stack.reverse()
