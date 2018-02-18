import unittest
from algorithms.ugraph import UGraph
from algorithms.bfs.bfs import BreadthFirstPaths
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Test for correct dfs between paths. 
You can see if there is a path between two nodes.
"""


class TestDFS(unittest.TestCase):
    def setUp(self):
        self.pairs = UGraph(100)
        for x in range(0, 98, 2):
            self.pairs.add_edge(x, x+2)

    def test_connecting(self):
        """Connect the pairs from 0 to 96, and see if they are connected."""
        self.d = BreadthFirstPaths(self.pairs, 0)
        self.assertTrue(self.d.hasPathTo(96))
        for i in range(1, 99, 2):
            self.assertFalse(self.d.hasPathTo(i))


if __name__ == '__main__':
    unittest.main()
