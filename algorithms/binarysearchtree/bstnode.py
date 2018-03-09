
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BSTNode:
    """"
    The representation of a node for a binary search tree
    """

    def __init__(self, item: tuple):
        self.left = None
        self.right = None
        self.item = item
