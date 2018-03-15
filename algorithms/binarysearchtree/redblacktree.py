from algorithms.binarysearchtree.rbtnode import RBTNode


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class RBT: #Red Black Tree
    """"
    A clean implementation of a Red Black Tree
    """
    RED = True
    BLACK = False

    def __init__(self):
        self.root = None
        self.inorder_arr = []

    def __iter__(self):
        self.inorder_arr = []
        self.i = 0
        self._inorderhelper(self.root)
        return self
        
    def __next__(self):
        if self.i > len(self.inorder_arr) - 1:
            raise StopIteration
        ret = self.inorder_arr[self.i]
        self.i += 1
        return ret

    def _inorderhelper(self, node:RBTNode ):
        if node == None:
            return
        self._inorderhelper(node.left)
        self.inorder_arr.append(node.item)
        self._inorderhelper(node.right)

    def isRed(self, node):
        if node is None:
            return False


    def put(self, item: tuple):
        self.root = self._put_helper(self.root, item)

    def _put_helper(self, node: RBTNode,  item: tuple) -> RBTNode:
        if node == None:
            return RBTNode(item, RBT.RED)
    

   