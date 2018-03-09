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

    def test_all_letters(self):
        for k, v in enumerate(list(map(chr, range(97, 123)))):
            self.secondbst.put((k, v))
        for k, _ in enumerate(list(map(chr, range(97, 123)))):
            self.assertIsNotNone(self.secondbst.get(k))
        for k, _ in enumerate(list(map(chr, range(124, 200)))):
            self.assertIsNone(self.bst.get(k))

    def test_some_equal_elements(self):
        for _, v in enumerate(list(map(chr, range(97, 123)))):
            self.bst.put((chr(97), v))
        self.assertIsNotNone(self.bst.get(chr(97)))


if __name__ == '__main__':
    unittest.main()
