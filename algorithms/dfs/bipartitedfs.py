from algorithms.ugraph import UGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class BipartiteDFS:
    """"
    This class checks whether a graph G is bipartite.
    """

    def __init__(self, g: UGraph):
        self.isBipartite = True
        self.color = [False]*g.V
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.g = g
        self.odd_cycle = []
        for i in range(0, g.V):
            if not self.marked[i]:
                self.dfs(self.g, i)
        self.check(self.g)

    def dfs(self, g, v: int):
        self.marked[v] = True
        for node in g.close(v):
            # We found an odd cycle graph
            if self.odd_cycle:
                return

            if not self.marked[node]:
                self.edgeTo[node] = v
                self.color[node] = not self.color[v]
                self.dfs(g, node)
            elif self.color[v] == self.color[node]:
                # Whoa, we found a odd-cycle graph dude.
                self.isBipartite = False
                self.odd_cycle.append(node)
                x = v
                while x != v:
                    self.odd_cycle.append(x)
                    x = self.edgeTo[x]
                self.odd_cycle.append(node)

    def check(self, g):
        if self.isBipartite:
            for node_index in range(0, self.g.V):
                for adj_node in g.close(node_index):
                    if self.color[node_index] == self.color[adj_node]:
                        raise "Wait, this isn't bipartite"

    def whatColor(self, v):
        return self.color[v]
