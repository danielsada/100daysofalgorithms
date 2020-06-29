from algorithms.digraph import DiGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

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
        self.hasCycle = lambda: len(self.cycle) == 0
        for s in range(0, g.V):
            if not self.marked[s] and self.cycle:
                self.dfs(g, s)

    def dfs(self, g: DiGraph, i: int):
        self.onStack[i] = True
        self.marked[i] = True
        for node in g.close(i):
            if self.hasCycle:
                # short circuit if cycle
                return
            elif not self.marked[i]:
                self.edgeTo[node] = i
                self.dfs(g, node)
            elif self.onStack[node]:
                # There is a cycle
                cycle = []
                init = i
                while init != node:
                    cycle.append(init)
                    init = self.edgeTo[init]
                cycle.append(node)
                return cycle
        self.onStack[i] = False
