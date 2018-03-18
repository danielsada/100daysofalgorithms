
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class Edge:
    """"
    An edge between two nodes
    """

    def __init__(self, v: int, w: int, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self) -> int:
        return self.v

    def other(self, i) -> int:
        if i == self.v:
            return self.w
        else:
            return self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight
