import unittest
from ugraph import UGraph

class TestUGraph(unittest.TestCase):
    def setUp(self):
        self.a = UGraph(1001)
        self.b = UGraph(100)

    def test_connecting(self):
        "We'll connect 1 node to 999 nodes and expect the len of adj to be 999"
        self.assertEqual(len(self.a.adj[0]),0)
        for i in range(1,1000):
            self.a.add_edge(0,i)
        self.assertEqual(len(self.a.adj[0]),  999)
        self.assertEqual(UGraph.degree(self.a,0), 999)

if __name__ == '__main__':
    unittest.main()