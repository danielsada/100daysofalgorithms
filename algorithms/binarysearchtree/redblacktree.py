"""
An implementation of Red Black Tree.
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"
"""
from algorithms.binarysearchtree.rbtnode import RBTNode


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
A clean implementation of a Red Black Tree
"""


class RedBlackTree:  # Red Black Tree
    RED = True
    BLACK = False

    def __init__(self):
        self.root = None
        self.inorder_arr = []
        self.i = 0

    def __iter__(self):
        self.inorder_arr = []
        self.i = 0
        self._inorderHelper(self.root)
        return self

    def __next__(self):
        if self.i > len(self.inorder_arr) - 1:
            raise StopIteration
        ret = self.inorder_arr[self.i]
        self.i += 1
        return ret

    def _inorderHelper(self, node: RBTNode):
        if node is None:
            return
        self._inorderHelper(node.left)
        self.inorder_arr.append(node.item)
        self._inorderHelper(node.right)

    def isRed(self, node):
        if node is None:
            return False
        return node.color == self.RED

    def _rotateLeft(self, node: RBTNode):
        assert self.isRed(node.right)
        child_node: RBTNode = node.right
        node.right = child_node.left
        child_node.left = node
        child_node.color = node.color
        node.color = self.RED
        return child_node

    def _rotateRight(self, node: RBTNode):
        assert self.isRed(node.left)
        child_node: RBTNode = node.left
        node.left = child_node.right
        child_node.right = node
        child_node.color = node.color
        node.color = self.RED
        return child_node

    def _flipColors(self, node: RBTNode):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def put(self, item: tuple):
        self.root = self._putHelper(self.root, item)
        if self.root is not None:
            self.root.color = self.BLACK

    def _putHelper(self, node: RBTNode, item: tuple) -> RBTNode:
        if node is None:
            return RBTNode(item, self.RED)
        xk, _ = node.item
        k, _ = item
        if k < xk:
            node.left = self._putHelper(node.left, item)
        elif k > xk:
            node.right = self._putHelper(node.right, item)
        else:
            node.item = item

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self._rotateLeft(node)
        if self.isRed(node.left) and node.left and self.isRed(node.left.left):
            node = self._rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self._flipColors(node)

        return node

    def delete(self, key):
        assert key != None
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = self.RED
        self.root = self._deleteHelper(self.root, key)

    def _deleteHelper(self, node: RBTNode, key):
        nk, _ = node.item
        if key < nk:
            if not self.isRed(node.left) and not self.isRed(node.left.left):
                node = self._moveRedLeft(node)
            node.left = self._deleteHelper(node.left, key)
        else:
            if self.isRed(node.left):
                node = self._rotateRight(node)
            if key == nk and node.right is None:
                return None
            if not self.isRed(node.right) and not self.isRed(node.right.left):
                node = self._moveRedRight(node)
            if key == nk:
                x: RBTNode = self.minimum(node.right)
                node.item = x.item
                node.right = self.deleteMinimum(node.right)
            else:
                node.right = self._deleteHelper(node.right, key)
        return self._balance(node)

    def _moveRedLeft(self, node):
        assert node != None  # noqa: E711
        assert self.isRed(node) and not self.isRed(
            node.left) and not self.isRed(node.left.left)
        self._flipColors(node)
        if not self.isRed(node.right.left):
            node.right = self._rotateRight(node.right)
            node = self._rotateLeft(node)
            self._flipColors(node)
        return node

    def _moveRedRight(self, node):
        assert node != None
        assert self.isRed(node) and not self.isRed(
            node.right) and not self.isRed(node.right.left)
        self._flipColors(node)
        if self.isRed(node.left.left):
            node = self._rotateRight(node)
            self._flipColors(node)
        return node

    @staticmethod
    def minimum(node):
        if node.left is None:
            return node
        else:
            return node.left

    def deleteMinimum(self, node):
        if node.left is None:
            return None
        if self.isRed(node.left) and not self.isRed(node.left.left):
            node = self._moveRedLeft(node)
        node.left = self.deleteMinimum(node.left)
        return self._balance(node)

    def _balance(self, node):
        if self.isRed(node.right):
            node = self._rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self._rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self._flipColors(node)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node

    @staticmethod
    def size(node):
        if node is None or node.count is None:
            return 0
        return node.count

    def get(self, key):
        """Returns None if not present"""
        x = self.root
        while x != None:
            if x.item[0] > key:
                x = x.left
            elif x.item[0] < key:
                x = x.right
            else:
                return x.item
        return None

    def getMaxElem(self):
        elem = self.root
        while elem is not None and elem.right is not None:
            elem = elem.right
        return elem.item

    def getMinElem(self):
        elem = self.root
        while elem is not None and elem.left is not None:
            elem = elem.left
        return elem.item

    # def deleteMin(self):
    #     if not self.isRed(self.root.left) and not self.isRed(self.root.right):
    #         self.root.color = self.RED
    #     self.root = self._deleteMinHelper(self.root)

    # def _deleteMinHelper(self, node):
    #     if node.left is None:
    #         return None
    #     if not self.isRed(node.left) and not self.isRed(node.left.left):
    #         node = self._moveRedLeft(node)
    #     node.left = self._deleteMinHelper(node.left)
    #     return self._balance(node)
