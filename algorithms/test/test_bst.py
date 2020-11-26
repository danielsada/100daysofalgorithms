import unittest
from algorithms.binarysearchtree.bst import BinarySearchTree

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Test Binary search trees.
Run uts with 
python -m unittest algorithms.test.test_bst

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
        self.forthBst = BinarySearchTree()
        self.alphaIterator = BinarySearchTree()
        for k, v in enumerate(list(map(chr, range(97, 123)))):
            self.alphaIterator.put((k, v))
        self.emptyTree = BinarySearchTree()

    def test_all_letters(self):
        """Test the alphabet darlin'"""
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
        """Test that we are overwriting our keys with new values."""
        for _, v in enumerate(list(map(chr, range(97, 123)))):
            self.bst.put((chr(97), v))
        self.assertIsNotNone(self.bst.get(chr(97)))

    def test_deletion(self):
        """Test that when we delete a node, it really deletes"""
        test = BinarySearchTree()
        test.put(('a', "www"))
        test.put(('e', "www.e"))
        test.put(('w', "www.w"))
        test.delete('e')
        test.delete('w')
        test.delete('a')
        self.assertIsNone(test.get('e'))
        self.assertIsNone(test.get('w'))
        self.assertIsNone(test.get('a'))

    def test_bst_with_proven_example(self):
        """
        Tested with a known example that orders correctly.
        """
        self.forthBst.put(('S', 0))
        self.forthBst.put(('E', 1))
        self.forthBst.put(('A', 2))
        self.forthBst.put(('R', 3))
        self.forthBst.put(('C', 4))
        self.forthBst.put(('H', 5))
        self.forthBst.put(('E', 6))
        self.forthBst.put(('X', 7))
        self.forthBst.put(('A', 8))
        self.forthBst.put(('M', 9))
        self.forthBst.put(('P', 10))
        self.forthBst.put(('L', 11))
        self.forthBst.put(('E', 12))
        levelOrder = self.forthBst.levelOrder()
        # for elem in levelOrder:
        #     n, l, r = elem
        #     print('\n')
        #     print("\t", n)
        #     print(l, "\t", r)
        #     print("\n")
        self.assertEqual(len(levelOrder), 10)
        self.assertEqual(levelOrder[0], ('S', 0))
        self.assertEqual(levelOrder[9], ('P', 10))

    def test_iterator(self):
        listResult = []
        for elem in self.alphaIterator:
            listResult.append(elem[1])
        self.assertEqual(len(listResult), 26)

    def test_empty(self):
        self.assertIsNone(self.emptyTree.getMinElem())
        self.assertIsNone(self.emptyTree.getMaxElem())
        self.assertIsNone(self.emptyTree.floor('a'))
        self.assertIsNone(self.emptyTree.ceiling('z'))
        self.assertFalse(self.emptyTree.deleteMin())
        self.assertEqual(self.emptyTree.sizeAtRoot(), 0)


if __name__ == '__main__':
    unittest.main()
