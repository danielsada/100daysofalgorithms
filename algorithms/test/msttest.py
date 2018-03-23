import unittest
from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph
from algorithms.mst.prim import Prim
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
A file that tests data structures and algorithms related to MSTs
"""


class MstTest(unittest.TestCase):
    def test_small_graph(self):
        wG = WeightedGraph(8)
        wG.addEdge(Edge(4, 5, 0.35))
        wG.addEdge(Edge(4, 7, 0.37))
        wG.addEdge(Edge(5, 7, 0.28))
        wG.addEdge(Edge(0, 7, 0.16))
        wG.addEdge(Edge(1, 5, 0.32))
        wG.addEdge(Edge(0, 4, 0.38))
        wG.addEdge(Edge(2, 3, 0.17))
        wG.addEdge(Edge(1, 7, 0.19))
        wG.addEdge(Edge(0, 2, 0.26))
        wG.addEdge(Edge(1, 2, 0.36))
        wG.addEdge(Edge(1, 3, 0.29))
        wG.addEdge(Edge(2, 7, 0.34))
        wG.addEdge(Edge(6, 2, 0.40))
        wG.addEdge(Edge(3, 6, 0.52))
        wG.addEdge(Edge(6, 0, 0.58))
        wG.addEdge(Edge(6, 4, 0.93))
        p = Prim(wG)
        self.assertEqual(p.weight, 1.81)


if __name__ == '__main__':
    unittest.main()
