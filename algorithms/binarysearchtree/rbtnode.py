
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class RBTNode:
    """"
    The representation of a node for a red black tree node
    """

    def __init__(self, item: tuple, isRed=False):
        self.left = None
        self.right = None
        self.item = item
        self.count = None
        self.color = isRed
