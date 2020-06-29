from algorithms.weightedgraph.diedge import DiEdge
#!/usr/bin/env

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Implementation of a Undirected  Weighted Graph for further algorithm exercises.
"""


class DirectedWeightedGraph:
    def __init__(self, v: int):
        self.V = v
        self.adj = [None]*v
        for i in range(0, self.V):
            self.adj[i] = []

    def addEdge(self, e: DiEdge):
        v: int = e.From()
        self.adj[v].append(e)

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
