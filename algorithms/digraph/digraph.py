#!/usr/bin/env

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Implementation of a Directed Graph for further algorithm exercises.
"""


class DiGraph:
    def __init__(self, v: int):
        self.V = v
        self.adj = [None]*v
        for i in range(0, v):
            self.adj[i] = []

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)

    def close(self, v: int):
        return iter(self.adj[v])

    def numberEdges(self, v) -> int:
        return len(self.adj[v])

    @staticmethod
    def degree(G, v):
        Gdegree = 0
        for _ in G.close(v):
            Gdegree += 1
        return Gdegree

    def reverse(self):
        rev = DiGraph(self.V)
        for v in range(0, self.V):
            for n in self.close(v):
                rev.addEdge(n, v)
        return rev
