
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class FlowNetWork:
    """"
    Describes a edge that has a capacity and a flow.
    """

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = []
        for i in range(0, self.V):
            self.adj[i] = []

    def __repr__(self):
        f = "FlowNetwork: \n"
        for i in range(self.V):
            f += f"Nodes From {i}: \n"
            for e in self.adj[i]:
                f += e.__repr__()
        return f

    def addEdge(self, e):
        v = e.source()
        w = e.destination()
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def edges(self):
        for i in range(self.V):
            for e in self.adj[i]:
                yield e
