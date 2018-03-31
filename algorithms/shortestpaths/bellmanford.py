import math
from collections import defaultdict
from algorithms.weightedgraph.diweightedgraph import DirectedWeightedGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BellmanFord:
    """"
    Bellman ford algorithm for shortest paths with negative weights. Also for detecting negative cycles
    """

    def __init__(self, g: DirectedWeightedGraph, start: int):
        self.g = g
        self.distTo = [math.inf] * self.g.V
        self.edgeTo = defaultdict(list)
        self.isQueued = [False] * self.g.V
        self.distTo[start] = 0.0
        self.q = []
        self.q.append(start)
        self.timesRelaxed = 0
        while self.q:
            v = self.q.pop(0)
            self.isQueued[v] = False
            self.relax(v)

    def relax(self, v):
        for e in self.g.adj[v]:
            w = e.To()
            if self.distTo[w] > (self.distTo[v] + e.weight):
                self.distTo[w] = self.distTo[v] + e.weight
                self.edgeTo[w] = e
                if not self.isQueued[w]:
                    self.q.append(w)
                    self.isQueued[w] = True
            self.timesRelaxed += 1

    def hasPathTo(self, v):
        return self.distTo[v] < math.inf

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        de = []
        e = self.edgeTo[v]
        while e is not None and e:
            de.append(e)
            e = self.edgeTo[e.From()]
        return de
