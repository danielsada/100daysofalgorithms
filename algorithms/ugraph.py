#!/usr/bin/env 
from collections import Counter

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implementation of a Undirected Graph for further algorithm exercises.
"""

class UGraph:
    def __init__(self, v:int):
        self.V = v
        self.adj = [None]*100
        for i in range(0,v):
            self.adj[i] = [];
    
    def add_edge(self,v:int,w:int):
        self.adj[v].append(w)   
        self.adj[w].append(v)
    
    def close(self,v:int):
        return iter(self.adj[v])
    
    def num_V(self):
        return len(self.adj)
    
    def num_E(self,v):
        return len(self.adj[v])
    
    @staticmethod
    def degree(G: UGraph, v: int):
        Gdegree = 0
        for connections in G.close(v):
            Gdegree+=1
        return Gdegree


g = UGraph(10);

g.add_edge(2,4);
g.add_edge(2,6);
g.add_edge(2,8);
g.add_edge(2,9);
for e in g.close(2):
    print(e)