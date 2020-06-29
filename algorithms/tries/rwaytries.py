
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
For this R-way tree we'll asume R = 256 (Extended ascii)
"""


class RTrieNode:
    """
    A node of an R way Trie.
    """

    def __init__(self, value=None):
        self.value = value
        self.next = [None]*256


class RWayTrie:
    """"
    A trie with R characters as links
    for demo purposes, using a dictionary is better.
    """
    R = 256
    n = 0

    def __init__(self):
        self.root = RTrieNode()

    def put(self, key, val):
        self.root = self._puthelper(self.root, key, val, 0)

    def _puthelper(self, x: RTrieNode, key, val, d):
        if x is None:
            x = RTrieNode()
        if d == len(key):
            if x.value is None:
                self.n += 1
            x.value = val
            return x
        c = key[d]
        x.next[ord(c)] = self._puthelper(x.next[ord(c)], key, val, d+1)
        return x

    def get(self, key):
        x = self._get(self.root, key, 0)
        return x.value if x is not None else None

    def contains(self, key):
        return self.get(key) is not None

    def _get(self, x, key, d):
        if x is None or d == len(key):
            return x
        c = key[d]
        return self._get(x.next[ord(c)], key, d+1)
