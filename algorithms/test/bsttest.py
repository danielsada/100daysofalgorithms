import unittest
from algorithms.binarysearchtree.bst import BinarySearchTree

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Test Binary search trees.
"""


class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.secondbst = BinarySearchTree()
        for k, v in enumerate(list(map(chr, range(97, 123)))):
            self.secondbst.put((k, v))
        self.thirdbst = BinarySearchTree()
        self.thirdbst.put(('a', "wowfriend"))
        self.thirdbst.put(('d',"more friendo"))
        self.thirdbst.put(('j',"incredible"))


    def test_all_letters(self):
        for k, _ in enumerate(list(map(chr, range(97, 123)))):
            self.assertIsNotNone(self.secondbst.get(k))
        for k, _ in enumerate(list(map(chr, range(124, 200)))):
            self.assertIsNone(self.bst.get(k))


    """Test min and max elements of a bst"""
    def test_min_max(self):
        _, mx = self.secondbst.max_elem()
        _, minx = self.secondbst.min_elem()
        self.assertEqual(mx, 'z')
        self.assertEqual(minx, 'a')
        self.secondbst.deleteMin();
        self.secondbst.deleteMin();
        _, minx = self.secondbst.min_elem()
        self.assertEqual(minx, 'c')


    """Test size. Size returns the amount of nodes rooted below a node."""
    def test_size(self):
        self.assertEqual(self.thirdbst.size_at_root(), 2)
        

    """Gives the closest node (down) to myself"""
    def test_floor(self):
        self.assertEqual(self.thirdbst.floor('e'), ('d',"more friendo"))
        # self.assertEqual(minx, 'a')

    """Gives the closest node (up) to myself"""
    def test_ceiling(self):
        self.assertEqual(self.thirdbst.ceiling('e'), ('j',"incredible"))

    def test_some_equal_elements(self):
        for _, v in enumerate(list(map(chr, range(97, 123)))):
            self.bst.put((chr(97), v))
        self.assertIsNotNone(self.bst.get(chr(97)))


if __name__ == '__main__':
    unittest.main()
