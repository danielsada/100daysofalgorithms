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
        self.thirdbst.put(('d', "more friendo"))
        self.thirdbst.put(('j', "incredible"))

    def test_all_letters(self):
        for k, _ in enumerate(list(map(chr, range(97, 123)))):
            self.assertIsNotNone(self.secondbst.get(k))
        for k, _ in enumerate(list(map(chr, range(124, 200)))):
            self.assertIsNone(self.bst.get(k))

    def test_min_max(self):
        """Test min and max elements of a bst"""
        _, mx = self.secondbst.getMaxElem()
        _, minx = self.secondbst.getMinElem()
        self.assertEqual(mx, 'z')
        self.assertEqual(minx, 'a')
        self.secondbst.deleteMin()
        self.secondbst.deleteMin()
        _, minx = self.secondbst.getMinElem()
        self.assertEqual(minx, 'c')

    def test_size(self):
        """Test size. Size returns the amount of nodes rooted below a node."""
        self.assertEqual(self.thirdbst.sizeAtRoot(), 2)

    def test_floor(self):
        """Gives the closest node (down) to myself"""
        self.assertEqual(self.thirdbst.floor('e'), ('d', "more friendo"))
        # self.assertEqual(minx, 'a')

    def test_ceiling(self):
        """Gives the closest node (up) to myself"""
        self.assertEqual(self.thirdbst.ceiling('e'), ('j', "incredible"))

    def test_some_equal_elements(self):
        for _, v in enumerate(list(map(chr, range(97, 123)))):
            self.bst.put((chr(97), v))
        self.assertIsNotNone(self.bst.get(chr(97)))

    def test_deletion(self):
        test = BinarySearchTree()
        test.put(('a', "www"))
        test.put(('e', "www.e"))
        test.put(('w', "www.w"))
        test.delete('e')


if __name__ == '__main__':
    unittest.main()
