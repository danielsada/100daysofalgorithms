#!/usr/bin/env 

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implementation of QuickUnion
Complexity:
Initialize => O(n)
Union      => O(n)
Connected  => O(n)
"""

class QuickUnion(object):
    def __init__(self, n):
        self.id = [None]*n
        for i in range(0, n):
            self.id[i] = i

    def root(self , i) -> int:
        while self.id[i] != i:
            i = self.id[i]
        return i
            
    def connected(self, a:int, b:int) -> bool:
        return self.root(a) == self.root(b)

    def union(self, a:int, b:int):      
        a_id:int = self.root(a)
        b_id:int = self.root(b)
        self.id[a_id] = b_id

