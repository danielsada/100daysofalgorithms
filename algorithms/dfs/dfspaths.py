from algorithms.ugraph import UGraph
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class DepthFirstPaths:
    """"
    Finds a path between start s, and all other indexes. 
    Then query it to see if there is a path between two nodes.
    """
    def __init__(self, g: UGraph, s: int):
        self.marked:List[bool] = [False]*g.num_V()
        self.edgeTo:List[int] = [None]*g.num_v();
        self.s = s; 
        self.dfs(g,s)
    
    def dfs(self, g, v:int):
        self.marked[v] = True
        for node in g.close(v):
            if not self.marked[node]:
                self.dfs(g, node);
                self.edgeTo[node] = v




