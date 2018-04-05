
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
For this R-way tree we'll asume R = 256 (Extended ascii)

"""


class TSTrieNode:
    """
    A node of an R way Trie.
    """

    def __init__(self, value=None):
        self.c = None
        self.value = value
        self.left: TSTrieNode = None
        self.mid: TSTrieNode = None
        self.right: TSTrieNode = None


class TSTrie:
    """"
    An efficient  Ternary search trie.
    It has three links per each node, and searches. 
    """

    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x: TSTrieNode, key, val, d):
        c = key[d]
        if x is None:
            x = TSTrieNode()
            x.c = c
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self._put(x.mid, key, val, d+1)
        else:
            x.value = val
        return x

    def get(self, key):
        x = self._get(self.root, key, 0)
        return x.value if x is not None else None

    def contains(self, key):
        return self.get(key) is not None

    def _get(self, x, key, d):
        if x is None:
            return None
        c = key[d]
        if ord(c) < ord(x.c):
            return self._get(x.left, key, d)
        elif ord(c) > ord(x.c):
            return self._get(x.right, key, d)
        elif d < len(key) - 1:
            return self._get(x.mid, key, d+1)
        else:
            return x
