from algorithms.binarysearchtree.bstnode import BSTNode


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BinarySearchTree:
    """"
    Description
    """

    def __init__(self):
        self.root = None

    def put(self, elem: tuple):
        pass

    """Returns None if not present"""

    def get(self, key) -> tuple | None:
        x = self.root
        while x != None:
            if x.item[0] > key:
                x = x.left
            elif x.item[0] < key:
                x = x.right
            else:
                return x.item
        return None

    def delete(self, key):
        pass

    def iterable(self, key) -> iter:
        pass
