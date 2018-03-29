import math
from collections import defaultdict
from algorithms.weightedgraph.diedge import DiEdge
from algorithms.weightedgraph.diweightedgraph import DirectedWeightedGraph
from algorithms.priorityqueue.indexminpq import IndexMinPQ

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class DijkstraSP:
    """"
    Shortest path API container
    """

    def __init__(self, G: DirectedWeightedGraph, start: int):
        self.g = G
        self.distTo = [math.inf] * G.V
        self.edgeTo = defaultdict(list)
        self.distTo[start] = 0.0

        self.pq = IndexMinPQ(G.V)
        self.pq.insert(start, self.distTo[start])

        while len(self.pq) > 0:  # pylint: disable=C1801
            v = self.pq.delMin()
            for edge in self.g.adj[v]:
                self.relax(edge)
        # assert self.verifySP(start)

    def relax(self, edge: DiEdge):
        v, w = edge.From(), edge.To()
        if self.distTo[w] > (self.distTo[v] + edge.weight):
            self.distTo[w] = self.distTo[v] + edge.weight
            self.edgeTo[w] = edge
            if self.pq.contains(w):
                self.pq.change_key(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])

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

    def verifySP(self, s):
        """
        We have to verify three things according to sedgewick
        1) for all edges (e) distTo[e.to()] <= distTo[e.from()] + e.weight()
        2) for all edges (e) on spt => istTo[e.to()] == distTo[e.from()] + e.weight()
        """
        for e in self.g.edges():
            if e.weight < 0:
                return False

        if self.distTo[s] and self.edgeTo[s] != None:
            return False

        for v in range(self.g.V):
            if v == s:
                continue
            if self.edgeTo[v] is None and self.distTo[v] != math.inf:
                return False

        for v in range(self.g.V):
            for e in self.g.adj[v]:
                w = e.To()
                if (self.distTo[v] + e.weight) < self.distTo[w]:
                    return False

        for w in range(self.g.V):
            if self.edgeTo[w] is None:
                continue
            e = self.edgeTo[w]
            v = e.From()
            if w != e.To():
                return False
            if self.distTo[v] + e.weight != self.distTo[w]:
                return False

        return True
