import unittest
from algorithms.ugraph import UGraph
from algorithms.dfs.dfs import DepthFirstPaths
from algorithms.dfs.bipartitedfs import BipartiteDFS
from algorithms.dfs.connected_components import ConnectedComponents
from algorithms.digraph.digraph import DiGraph
from algorithms.dfs.topologicalsort import TopologicalSort


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
        graph = UGraph(4)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        self.bipartite = BipartiteDFS(graph)
        nonbiGraph = UGraph(4)
        nonbiGraph.add_edge(0, 1)
        nonbiGraph.add_edge(1, 2)
        nonbiGraph.add_edge(2, 3)
        nonbiGraph.add_edge(0, 2)
        nonbiGraph.add_edge(0, 3)
        self.notbipartite = BipartiteDFS(nonbiGraph)

    def test_connecting(self):
        """Connect the pairs from 0 to 96, and see if they are connected."""
        self.d = DepthFirstPaths(self.pairs, 0)
        self.assertTrue(self.d.hasPathTo(96))
        for i in range(1, 99, 2):
            self.assertFalse(self.d.hasPathTo(i))

    def test_bipartite(self):
        self.assertTrue(self.bipartite.isBipartite)
        self.assertFalse(self.notbipartite.isBipartite)


class ConnectedComponentsTest(unittest.TestCase):
    def setUp(self):
        self.graphArr = []
        for g in range(1, 200):
            self.graphArr.append(UGraph(g))

        self.ccarr = []
        for c in range(0, 199):
            self.ccarr.append(ConnectedComponents(self.graphArr[c]))

    def test_cc(self):
        for cc in self.ccarr:
            self.assertEqual(cc.count(), cc.g.V)

    def test_cc_integrity(self):
        g = UGraph(20)
        count = 2
        for i in range(1, 10):
            count += 1
            g.add_edge(i, i+1)
        self.integrity = ConnectedComponents(g)
        self.assertEqual(count, self.integrity.count())


class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.d = DiGraph(7)
        self.d.add_edge(0, 5)
        self.d.add_edge(0, 2)
        self.d.add_edge(0, 1)
        self.d.add_edge(3, 6)
        self.d.add_edge(3, 5)
        self.d.add_edge(3, 4)
        self.d.add_edge(5, 2)
        self.d.add_edge(6, 4)
        self.d.add_edge(6, 0)
        self.d.add_edge(3, 2)
        self.d.add_edge(1, 4)

    def test_topological(self):
        self.t = TopologicalSort(self.d)
        torder = self.t.get_topological()
        self.assertEqual(torder, [3, 6, 0, 1, 4, 5, 2])


if __name__ == '__main__':
    unittest.main()
