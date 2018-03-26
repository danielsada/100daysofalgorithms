import math
from collections import defaultdict
from algorithms.weightedgraph.diedge import DiEdge
from algorithms.weightedgraph.diweightedgraph import DirectedWeightedGraph
from algorithms.priorityqueue.priorityqueue import PriorityQueue

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class DijkstraSP:
    """"
    Shortest path API container
    """

    def __init__(self, G: DirectedWeightedGraph, start: int):
        self.distTo = [math.inf] * G.V
        self.edgeTo = defaultdict(list)
        self.distTo[start] = 0.0
        self.pq = PriorityQueue(False)
        self.pq.add((self.distTo[start], start))
        while self.pq:
            (_, i) = self.pq.pop()
            for edge in G.adj[i]:
                self.relax(edge)

    def relax(self, edge: DiEdge):
        pass
