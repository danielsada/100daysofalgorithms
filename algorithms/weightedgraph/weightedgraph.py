from algorithms.weightedgraph.edge import Edge
#!/usr/bin/env

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implementation of a Undirected  Weighted Graph for further algorithm exercises.
"""


class WeightedGraph:
    def __init__(self, v: int):
        self.V = v
        self.adj = [None]*v
        for i in range(0, self.V):
            self.adj[i] = []

    def addEdge(self, e: Edge):
        v: int = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)

    def close(self, v: int):
        return iter(self.adj[v])

    def numEdges(self, v) -> int:
        return len(self.adj[v])

    def edges(self):
        edgelist = []
        for i in range(0, self.V):
            for e in self.adj[i]:
                edgelist.append(e)
        return edgelist

    @staticmethod
    def degree(G, v):
        Gdegree = 0
        for _ in G.close(v):
            Gdegree += 1
        return Gdegree
