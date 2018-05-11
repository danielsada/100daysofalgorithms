from algorithms.minflow.flownetwork import FlowNetwork

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class FordFulkerson:
    """"
    An implementation of Max Flow
    """

    def __init__(self, g: FlowNetwork, s, t):
        """ S is the source vertex, t is the sink vertex."""
        self.V = g.V()
        self.marked = [False]*self.V
        self.edgeTo = []*self.V
        self.value = 0.0


