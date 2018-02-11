import unittest
from quickfind import QuickFind

class TestQuickFind(unittest.TestCase):
    def setUp(self):
        self.a = QuickFind(10)

    def test_integrity(self):
        self.a.union(1,3)
        self.a.union(3,5)
        self.a.union(5,7)
        self.assertEqual(self.a.connected(1,7), True)

if __name__ == '__main__':
    unittest.main()