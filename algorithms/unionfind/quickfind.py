#!/usr/bin/env

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implements the QuickFind algorithm for connected nodes.
Complexity:
Initialize => O(n)
Union      => O(n)
Connected  => O(1)
"""


class QuickFind(object):
    def __init__(self, n):
        self.id = [None]*n
        for i in range(0, n):
            self.id[i] = i

    def connected(self, a: int, b: int) -> bool:
        return self.id[a] == self.id[b]

    def union(self, a: int, b: int):
        a_id: int = self.id[a]
        b_id: int = self.id[b]
        for i, _ in enumerate(self.id):
            if self.id[i] == a_id:
                self.id[i] = b_id
