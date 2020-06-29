
from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph
from algorithms.priorityqueue.priorityqueue import PriorityQueue

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class Prim:
    """"
    Implements Prim's algorithm for finding the minimum spanning tree.
    """

    def __init__(self, g: WeightedGraph):
        self.g = g
        self.mst = []
        self.marked = [False]*self.g.V
        self.pq = PriorityQueue(False)
        self.weight = 0
        self.lazyPrim(self.g)

    def lazyPrim(self, graph):
        for v in range(0, self.g.V):
            if not self.marked[v]:
                self.prim(graph, v)  # Generates Minimum spanning forest.

    def prim(self, g, start):
        self.scan(g, start)
        while len(self.pq) > 0:
            e = self.pq.pop()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append(e)
            self.weight += e.weight
            if not self.marked[v]:
                self.scan(g, v)
            if not self.marked[w]:
                self.scan(g, w)

    def scan(self, g, v):
        # print("Current pq, ", self.pq.pq.elements)
        self.marked[v] = True
        for e in g.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.add(e)
