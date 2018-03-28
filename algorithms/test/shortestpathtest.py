import unittest
from algorithms.weightedgraph.diweightedgraph import DirectedWeightedGraph
from algorithms.weightedgraph.diedge import DiEdge
from algorithms.shortestpaths.dijkstra import DijkstraSP


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""

"""


class TestSP(unittest.TestCase):
    def setUp(self):
        # g = WeightedGraph(10)
        # g.addEdge(Edge(0, 2, 0.1))
        # g.addEdge(Edge(0, 3, 0.1))
        # g.addEdge(Edge(9, 0, 0.1))
        # g.addEdge(Edge(0, 1, 0.1))
        # g.addEdge(Edge(1, 9, 0.1))

        # g.addEdge(Edge(2, 8, 0.1))
        # g.addEdge(Edge(3, 7, 0.1))
        # g.addEdge(Edge(4, 6, 0.1))
        # g.addEdge(Edge(3, 4, 0.1))
        # g.addEdge(Edge(4, 1, 0.1))

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
        d = DijkstraSP(self.anotherOne, 0)
        for t in range(1, self.anotherOne.V):
            print(f"Testing {t} connections")
            if d.hasPathTo(t):
                print(f"0 => {t} d = {d.distTo[t]}")
                print(d.pathTo(t))
            else:
                print("no path bro")


if __name__ == '__main__':
    unittest.main()
