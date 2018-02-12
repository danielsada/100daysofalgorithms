#!/usr/bin/env 

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implementation of PathFlattened Union Find
Complexity:
Initialize => O(n)
Union      => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
Connected  => O( N + M lg* N) (about linear in practice as lg* of N^65536 is 5)
"""

class PathFlattenedUnionFind(object):
    def __init__(self, n):
        self.id = [None]*n
        self.sz = [1]*n
        for i in range(0, n):
            self.id[i] = i

    def root(self , i) -> int:
        while self.id[i] != i:
            self.id[i]  = self.id[self.id[i]]
            i = self.id[i]
        return i
            
    def connected(self, a:int, b:int) -> bool:
        return self.root(a) == self.root(b)

    def union(self, a:int, b:int):      
        a_id:int = self.root(a)
        b_id:int = self.root(b)
        if self.sz[a_id] > self.sz[b_id]:
            self.sz[a_id] += self.sz[b_id] 
            self.id[b_id] = a_id
        else:
            self.sz[b_id] += self.sz[a_id] 
            self.id[a_id] = b_id

