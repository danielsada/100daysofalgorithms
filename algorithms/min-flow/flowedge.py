
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class FlowEdge:
    """"
    Describes a edge that has a capacity and a flow.
    """

    def __init__(self, v, w, capacity, flow=0.0, epilson=0.0001):
        self.v = v
        self.w = w
        self.cap = capacity
        self.flow = flow
        self.epilson = epilson

    def __repr__(self):
        return f"FlowEdge: {self.v} => {self.w} with flow {self.flow} and capacity {self.cap}"

    def source(self):
        return self.v

    def destination(self):
        return self.w

    def other(self, vertex):
        assert (vertex == self.v or vertex == self.w)
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def residualCapacity(self, vertex):
        assert (vertex == self.v or vertex == self.w)
        if vertex == self.v:
            return self.flow
        else:
            return self.cap - self.flow

    def addResidualFlow(self, vertex, delta):
        assert (vertex == self.v or vertex == self.w)
        if vertex == self.v:
            self.flow -= delta
        else:
            self.flow += delta

        if abs(self.flow) <= self.epilson:
            self.flow = 0
        if abs(self.flow - self.cap) <= self.epilson:
            self.flow = self.cap
