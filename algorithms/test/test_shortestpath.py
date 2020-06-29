import unittest
from algorithms.weightedgraph.diweightedgraph import DirectedWeightedGraph
from algorithms.weightedgraph.diedge import DiEdge
from algorithms.shortestpaths.dijkstra import DijkstraSP
from algorithms.shortestpaths.bellmanford import BellmanFord

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
A little test for dijkstra
"""


class TestSP(unittest.TestCase):
    def setUp(self):
        aO = DirectedWeightedGraph(8)
        aO.addEdge(DiEdge(4, 5, 0.35))
        aO.addEdge(DiEdge(5, 4, 0.35))
        aO.addEdge(DiEdge(4, 7, 0.37))
        aO.addEdge(DiEdge(5, 7, 0.28))
        aO.addEdge(DiEdge(7, 5, 0.28))
        aO.addEdge(DiEdge(5, 1, 0.32))
        aO.addEdge(DiEdge(0, 4, 0.38))
        aO.addEdge(DiEdge(0, 2, 0.26))
        aO.addEdge(DiEdge(7, 3, 0.39))
        aO.addEdge(DiEdge(1, 3, 0.29))
        aO.addEdge(DiEdge(2, 7, 0.34))
        aO.addEdge(DiEdge(6, 2, 0.40))
        aO.addEdge(DiEdge(3, 6, 0.52))
        aO.addEdge(DiEdge(6, 0, 0.58))
        aO.addEdge(DiEdge(6, 4, 0.93))
        self.anotherOne = aO

    def test_dijkstra(self):
        weights = [0, 1.05, 0.26, 0.99, 0.38, 0.73, 1.51, 0.60]
        d = DijkstraSP(self.anotherOne, 0)
        for t in range(0, 8):
            if d.hasPathTo(t):
                self.assertAlmostEqual(d.distTo[t], weights[t], delta=0.01)

    def test_bellman_ford(self):
        weights = [0, 1.05, 0.26, 0.99, 0.38, 0.73, 1.51, 0.60]
        d = BellmanFord(self.anotherOne, 0)
        for t in range(0, 8):
            if d.hasPathTo(t):
                self.assertAlmostEqual(d.distTo[t], weights[t], delta=0.01)


if __name__ == '__main__':
    unittest.main()
