from algorithms.weightedgraph.edge import Edge
from algorithms.weightedgraph.weightedgraph import WeightedGraph
from algorithms.priorityqueue.priorityqueue import PriorityQueue
import unittest

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""

"""


class PrioirityQueueTest(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_simple(self):
        g = WeightedGraph(10)
        g.addEdge(Edge(0, 2, 0.1))
        g.addEdge(Edge(0, 3, 0.2))
        g.addEdge(Edge(9, 0, 0.3))
        g.addEdge(Edge(0, 1, 0.4))
        g.addEdge(Edge(1, 9, 0.5))

        g.addEdge(Edge(2, 8, 0.6))
        g.addEdge(Edge(3, 7, 0.7))
        g.addEdge(Edge(4, 6, 0.8))
        g.addEdge(Edge(3, 4, 0.9))
        g.addEdge(Edge(4, 1, 1.0))
        for edge in g.edges():
            self.pq.add(edge)
        for x in range(0, 9):
            self.pq.pop()
            self.assertAlmostEqual(self.pq.pop().weight,
                                   1 - (x*.10), delta=0.0000001)


if __name__ == '__main__':
    unittest.main()
