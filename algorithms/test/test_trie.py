import unittest
from algorithms.tries.rwaytries import RWayTrie
from algorithms.tries.tstries import TSTrie

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Testing tries.
"""


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.testsA = "she sells sea shells by the sea shore"

    def test_rtrie(self):
        """Testing RTrie with she sells sea shells by the sea shore"""
        a = RWayTrie()
        for i, v in enumerate(self.testsA.split(" ")):
            a.put(v, i)
        self.assertIsNotNone(a.get("sea"))
        self.assertIsNotNone(a.get("shells"))
        self.assertIsNotNone(a.get("by"))
        self.assertIsNotNone(a.get("the"))
        self.assertIsNone(a.get("mid"))

    def test_tst_trie(self):
        """Testing TSTrie with she sells sea shells by the sea shore"""
        a = TSTrie()
        for i, v in enumerate(self.testsA.split(" ")):
            a.put(v, i)
        self.assertIsNotNone(a.get("sea"))
        self.assertIsNotNone(a.get("shells"))
        self.assertIsNotNone(a.get("by"))
        self.assertIsNotNone(a.get("the"))
        self.assertIsNone(a.get("mid"))


if __name__ == '__main__':
    unittest.main()
