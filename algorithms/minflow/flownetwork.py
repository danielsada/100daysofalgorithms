
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"
from typing import List

from algorithms.minflow.flowedge import FlowEdge


class FlowNetwork:
    """"
    Describes a edge that has a capacity and a flow.
    """

    def __init__(self, v):
        assert v > 0
        self.V = v
        self.E = 0
        self.adj = [None] * v
        for i in range(0, v):
            self.adj[i] = []

    def __repr__(self):
        f = "FlowNetwork: \n"
        for i in range(self.V):
            f += f"Nodes From {i}: \n"
            for e in self.adj[i]:
                f += e.__repr__()
        return f

    def get_edges_for_node(self, v: int) -> List[FlowEdge]:
        return self.adj[v]

    def addEdge(self, e: FlowEdge):
        v = e.source()
        w = e.destination()
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1

    def edges(self):
        for i in range(self.V):
            for e in self.adj[i]:
                yield e

    
