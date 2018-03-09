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

    def put(self, item: tuple):
        self.root = self.put_rec(self.root, item)

    def put_rec(self, node: BSTNode,  item: tuple) -> BSTNode:
        if node == None:
            return BSTNode(item)

        k = item[0]
        n_key = node.item[0]

        if k < n_key:
            node.left = self.put_rec(node.left, item)
        elif k > n_key:
            node.right = self.put_rec(node.right, item)
        else:
            node.item = item
        return node

    """Returns None if not present"""

    def get(self, key):
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
