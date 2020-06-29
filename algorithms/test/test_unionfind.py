import unittest
from algorithms.unionfind.quickfind import QuickFind
from algorithms.unionfind.quickunion import QuickUnion
from algorithms.unionfind.weightedunionfind import WeightedUnionFind
from algorithms.unionfind.pathflattenedunionfind import PathFlattenedUnionFind


class TestQuickFind(unittest.TestCase):
    def setUp(self):
        self.a = QuickFind(10)
        self.b = QuickUnion(100)

    def test_integrity(self):
        self.a.union(1, 3)
        self.a.union(3, 5)
        self.a.union(5, 7)
        self.assertEqual(self.a.connected(1, 7), True)

    def test_zerotofifty(self):
        for n in range(1, 50):
            self.b.union(n, n+1)
        self.assertTrue(self.b.connected(2, 45))
        self.assertTrue(self.b.connected(1, 50))
        self.assertTrue(self.b.connected(25, 26))


class TestQuickUnion(unittest.TestCase):
    def setUp(self):
        self.a = QuickUnion(10)
        self.b = QuickUnion(100)

    def test_integrity(self):
        self.a.union(1, 3)
        self.a.union(3, 5)
        self.a.union(5, 7)
        self.assertTrue(self.a.connected(1, 7))

    def test_zerotofifty(self):
        for n in range(1, 50):
            self.b.union(n, n+1)
        self.assertTrue(self.b.connected(2, 45))
        self.assertTrue(self.b.connected(1, 50))
        self.assertTrue(self.b.connected(25, 26))


class TestWeightedUnionFind(unittest.TestCase):
    def setUp(self):
        self.a = WeightedUnionFind(10)
        self.b = WeightedUnionFind(100)

    def test_integrity(self):
        self.a.union(1, 3)
        self.a.union(3, 5)
        self.a.union(5, 7)
        self.assertTrue(self.a.connected(1, 7))

    def test_zerotofifty(self):
        for n in range(1, 50):
            self.b.union(n, n+1)
        self.assertTrue(self.b.connected(2, 45))
        self.assertTrue(self.b.connected(1, 50))
        self.assertTrue(self.b.connected(25, 26))


class TestPathFlattenedUnionFind(unittest.TestCase):
    def setUp(self):
        self.a = PathFlattenedUnionFind(10)
        self.b = PathFlattenedUnionFind(100)

    def test_integrity(self):
        self.a.union(1, 3)
        self.a.union(3, 5)
        self.a.union(5, 7)
        self.assertTrue(self.a.connected(1, 7))

    def test_zerotofifty(self):
        for n in range(1, 50):
            self.b.union(n, n+1)
        self.assertTrue(self.b.connected(2, 45))
        self.assertTrue(self.b.connected(1, 50))
        self.assertTrue(self.b.connected(25, 26))
        self.assertFalse(self.b.connected(1, 70))


if __name__ == '__main__':
    unittest.main()
