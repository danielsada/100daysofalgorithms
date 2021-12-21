from algorithms.minflow.flownetwork import FlowNetwork
from algorithms.shortestpaths.bellmanford import BellmanFord

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class FordFulkerson:
    """"
    An implementation of Max Flow
    """

    def __init__(self, g: FlowNetwork, s, t):
        """ S is the source vertex, t is the sink vertex."""
        self.V = g.V
        self.g = g
        self.marked = [False]*self.V
        self.edgeTo = []*self.V
        self.totalFlow = 0.0
        self.s = s
        self.t = t
    
    def maximum_flow(self):
        q = []
        q.append(self.s)
        while len(q) != 0:
            curr = q.pop()
            for e in self.g.get_edges_for_node(curr):
                e.addResidualFlow(e, 2)
                
                
        



