
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class DiEdge:
    """"
    A directed edge between two nodes.
    """

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __repr__(self):
        return f"dE ({self.v} => {self.w} w: {self.weight})"

    # Intentionally starting with F as from is reserved.
    def From(self):  # pylint:  disable=C0103
        return self.v

    # Intentionally uppercase starting, to keep convention here.
    def To(self):  # pylint:  disable=C0103
        return self.w
