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

    def test_all_letters(self):
        for k, _ in enumerate(list(map(chr, range(97, 123)))):
            self.assertIsNotNone(self.secondbst.get(k))
        for k, _ in enumerate(list(map(chr, range(124, 200)))):
            self.assertIsNone(self.bst.get(k))

    def test_min_max(self):
        _, mx = self.secondbst.max_elem()
        _, minx = self.secondbst.min_elem()
        self.assertEqual(mx, 'z')
        self.assertEqual(minx, 'a')

    @unittest.skip("""TODO: Improve this, this actually doesn't work quite well for this purpose
    Build another syntax tree.
    """)
    def test_floor(self):
        self.assertEqual(self.secondbst.floor((23, 'x'))[1], 'x')
        # self.assertEqual(minx, 'a')

    @unittest.skip("""TODO: Improve this, this actually doesn't work quite well for this purpose
    Build another syntax tree.
    """)
    def test_ceiling(self):
        self.assertEqual(self.secondbst.ceiling((23, 'x'))[1], 'x')

    def test_some_equal_elements(self):
        for _, v in enumerate(list(map(chr, range(97, 123)))):
            self.bst.put((chr(97), v))
        self.assertIsNotNone(self.bst.get(chr(97)))


if __name__ == '__main__':
    unittest.main()
