from algorithms.digraph.digraph import DiGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Detecting a cycle in an undirected graph using DFS.
Asumes no self loops.
"""


class DiCycle:
    def __init__(self, g):
        self.marked = [False] * g.V
        self.onStack = [False] * g.V
        self.edgeTo = [None]*g.V
        self.cycle = []
        self.hasCycle = False
        for s in range(0, g.V):
            if not self.marked[s] and len(self.cycle) == 0:
                self.dfs(g, s)

    # TODO finish this.
    def dfs(self, g, i: int):
        pass
