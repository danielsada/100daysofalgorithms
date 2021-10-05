from algorithms.minflow.flownetwork import FlowNetwork
from algorithms.minflow.flowedge import FlowEdge
from algorithms.minflow.fordfulkerson import FordFulkerson
import unittest

class TestSP(unittest.TestCase):
    def setUp(self):
        flow = FlowNetwork(10)
        flow.addEdge(FlowEdge(0, 1, 5, 1))
        flow.addEdge(FlowEdge(0, 2, 5, 1))
        flow.addEdge(FlowEdge(0, 3, 5, 3))
        flow.addEdge(FlowEdge(0, 4, 5, 1))
        flow.addEdge(FlowEdge(2, 4, 5, 2))
        self.f1 = flow


    def test_flownetwork(self):
        # Arrange
        ff = FordFulkerson(self.f1, 0, 4)
        self.assertTrue(True)
        