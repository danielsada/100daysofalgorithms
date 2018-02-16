from algorithms.ugraph import UGraph
from typing import List

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BreadthFirstPaths:
    """"
    This is a Breadth First Search.
    This will also calculate the distances 
    between the nodes preemptively.
    Finds a path between start s, and all other indexes. 
    Then query it to see if there is a path between two nodes.
    """

    def __init__(self, g: UGraph, s: int):
        self.queue = []
        self.queue.append(s)
