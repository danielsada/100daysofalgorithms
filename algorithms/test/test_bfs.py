import unittest
from algorithms.ugraph.ugraph import UGraph
from algorithms.bfs.bfs import BreadthFirstPaths

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Test for correct dfs between paths. 
You can see if there is a path between two nodes.
To run this file, you can do
python -m unittest algorithms.test.test_bfs
"""


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.pairs = UGraph(100)
        for x in range(0, 98, 2):
            self.pairs.addEdge(x, x+2)
        self.secondTest = UGraph(6)
        self.secondTest.addEdge(0, 1)
        self.secondTest.addEdge(1, 2)
        self.secondTest.addEdge(2, 3)

    def test_connecting(self):
        """Connect the pairs from 0 to 96, and see if they are connected."""
        self.d = BreadthFirstPaths(self.pairs, 0)
        self.assertTrue(self.d.hasPathTo(96))
        for i in range(1, 99, 2):
            self.assertFalse(self.d.hasPathTo(i))

    def test_zero_to_three(self):
        bfs = BreadthFirstPaths(self.secondTest, 0)
        self.assertTrue(bfs.hasPathTo(3))
        self.assertEqual(bfs.pathTo(3), [3, 2, 1, 0])
        self.assertFalse(bfs.hasPathTo(5))
        self.assertIsNone(bfs.pathTo(5))


if __name__ == '__main__':
    unittest.main()
