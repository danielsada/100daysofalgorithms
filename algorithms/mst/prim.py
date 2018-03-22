from typing import Iterator
from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph
from algorithms.mst.mst import Mst
from algorithms.priorityqueue.priorityqueue import PriorityQueue

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class Prim:
    """"
    Implements Prim's algorithm for finding the minimum spanning tree.
    """

    def __init__(self, g: WeightedGraph):
        self.g = g
        self.mst: Mst = Mst(WeightedGraph(g.E))
        self.pq = PriorityQueue()
        self.startGreedyMst(0)

    def startGreedyMst(self, init):
        curr_node = init
        while len(self.mst) != self.g.V - 1:
            for adj in self.g.adj(curr_node):
                self.pq.add(adj)
