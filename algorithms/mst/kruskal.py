from algorithms.unionfind.weightedunionfind import WeightedUnionFind
from algorithms.heaps.minheap import MinHeap
from algorithms.mst.mst import MST
from algorithms.weightedgraph.weightedgraph import WeightedGraph
from algorithms.weightedgraph.edge import Edge
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class Kruskal:
    """"
    Kruskal algorithm for finding a MST.
    Complexity of E log E
    Build list and sort => E log E
    Union = log* V (about 1 to 5)
    Connected = log* E (about 1 to 5)

    worst case complexity?
        E log E * log* V * log* E
    """

    def __init__(self, g: WeightedGraph):
        self.mst = MST(g)
        self.g = g
        self.edges = g.edges()
        self.edges.sort(key=lambda x: x.weight, reverse=True)
        self.uf = WeightedUnionFind(self.g.V)

    def kruskal(self):
        while len(self.edges) > 0 and len(self.mst.edgelist) < self.g.v - 1:
            pop_elem: Edge = self.edges.pop()
            a: int = pop_elem.either()
            b: int = pop_elem.other(a)
            if not self.uf.connected(a, b):
                self.uf.union(a, b)
                self.mst.edgelist.append(pop_elem)
