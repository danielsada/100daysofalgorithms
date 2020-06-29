__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class BSTNode:
    """"
    The representation of a node for a binary search tree
    """

    def __init__(self, item: tuple):
        self.left = None
        self.right = None
        self.item = item
        self.count = None
