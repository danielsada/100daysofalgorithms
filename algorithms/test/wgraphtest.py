from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph

import unittest

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""

"""


class WeightedGraphTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        g = WeightedGraph(10)
        g.addEdge(Edge(0, 2, 0.1))
        g.addEdge(Edge(0, 3, 0.1))
        g.addEdge(Edge(9, 0, 0.1))
        g.addEdge(Edge(0, 1, 0.1))
        g.addEdge(Edge(1, 9, 0.1))

        g.addEdge(Edge(2, 8, 0.1))
        g.addEdge(Edge(3, 7, 0.1))
        g.addEdge(Edge(4, 6, 0.1))
        g.addEdge(Edge(3, 4, 0.1))
        g.addEdge(Edge(4, 1, 0.1))
        sumWeights = 0
        for edge in g.edges():
            sumWeights += edge.weight
        self.assertAlmostEqual(sumWeights, 2.0, delta=.00001)


if __name__ == '__main__':
    unittest.main()
