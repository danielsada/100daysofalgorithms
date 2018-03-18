import unittest
from algorithms.digraph.digraph import DiGraph


class TestDigraph(unittest.TestCase):
    def setUp(self):
        self.d = DiGraph(5)

    def test_connecting(self):
        self.d.addEdge(0, 1)
        self.d.addEdge(1, 2)
        self.assertEqual(len(self.d.adj[2]), 0)
        self.assertEqual(len(self.d.adj[0]), 1)


if __name__ == '__main__':
    unittest.main()
