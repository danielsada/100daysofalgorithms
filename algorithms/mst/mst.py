from typing import Iterator
from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class Mst:
    """"
    A Minimum Spanning Tree representation, 
    which allows us to represent all the edges in it.
    """

    def __init__(self, g: WeightedGraph):
        self.g = g
        self.edgelist = []

    def __repr__(self):
        print(self.edgelist)

    def __len__(self):
        len(self.edgelist)

    def edges(self) -> Iterator(Edge):
        return iter(self.edgelist)

    def weight(self):
        sm = 0.0
        for edges in self.edges():
            sm += edges.weight
        return sm
