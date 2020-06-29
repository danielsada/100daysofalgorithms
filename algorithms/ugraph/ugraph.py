#!/usr/bin/env

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Implementation of a Undirected Graph for further algorithm exercises.
"""


class UGraph:
    def __init__(self, v: int):
        self.V = v
        self.adj = [None]*v
        for i in range(0, v):
            self.adj[i] = []

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def close(self, v: int):
        return iter(self.adj[v])

    def numEdges(self, v) -> int:
        return len(self.adj[v])

    @staticmethod
    def degree(G, v):
        Gdegree = 0
        for connections in G.close(v):
            Gdegree += 1
        return Gdegree
