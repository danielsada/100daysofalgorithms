from algorithms.binarysearchtree.bstnode import BSTNode


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BinarySearchTree:
    """"
    A clean implementation of Binary Search Trees.
    """

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

    def _inorderHelper(self, node: BSTNode):
        if node is None:
            return
        self._inorderHelper(node.left)
        self.inorder_arr.append(node.item)
        self._inorderHelper(node.right)

    def put(self, item: tuple):
        self.root = self._putHelper(self.root, item)

    def _putHelper(self, node: BSTNode, item: tuple) -> BSTNode:
        if node is None:
            return BSTNode(item)
        k, _ = item
        xk, _ = node.item
        if k < xk:
            node.left = self._putHelper(node.left, item)
        elif k > xk:
            node.right = self._putHelper(node.right, item)
        else:
            node.item = item
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node

    def get(self, key):
        """Returns None if not present"""
        x = self.root
        while x is not None:
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

    def floor(self, key):
        x = self._floorHelper(self.root, key)
        if x is None:
            return None
        return x.item

    def _floorHelper(self, node, key):
        if node is None:
            return None
        xk, _ = node.item
        if xk == key:
            return node
        if key < xk:
            return self._floorHelper(node.left, key)
        t = self._floorHelper(node.right, key)
        if t is not None:
            return t
        else:
            return node

    def ceiling(self, key):
        x = self._ceilingHelper(self.root, key)
        if x is None:
            return None
        return x.item

    def _ceilingHelper(self, node, key):
        if node is None:
            return None
        xk, _ = node.item
        if xk == key:
            return node
        if key < xk:
            t = self._ceilingHelper(node.right, key)
            if t is not None:
                return t
            else:
                return node
        return self._ceilingHelper(node.right, key)

    @staticmethod
    def size(node):
        if node is None or node.count is None:
            return 0
        return node.count

    def sizeAtRoot(self):
        return self.size(self.root)

    def deleteMin(self):
        self.root = self._deleteMinHelper(self.root)

    def _deleteMinHelper(self, node):
        if node.left is None:
            return node.right
        node.left = self._deleteMinHelper(node.left)
        node.count = self._computeSize(node)
        return node

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        xk, _ = node.item

        if key < xk:
            node.left = self._delete(node.left, key)
        elif key > xk:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            tempNode = node
            node = self._minelemfromNode(tempNode.right)
            node.right = self._deleteMinHelper(node)
            node.left = tempNode.left
        node.count = self._computeSize(node)
        return node

    def _minelemfromNode(self, node):
        if node.left is None:
            return node
        else:
            return self._minelemfromNode(node.left)

    def _computeSize(self, node):
        sz_node_right = self.size(node.right) if self.size(
            node.right) is not None else 0
        sz_node_left = self.size(node.left) if self.size(
            node.left) is not None else 0
        return 1 + sz_node_left + sz_node_right


# Alternative solution for floor:
    # def floor(self, item):
    #     if item is None:
    #         return None
    #     return self._floorhelper(self.root, item, None)

    # def _floorhelper(self, node, item, best):
    #     if node is None:
    #         return best
    #     _, v = node.item
    #     _, vo = item
    #     if vo < v:
    #         return self._floorhelper(node.left, item, best)
    #     elif vo > v:
    #         return self._floorhelper(node.right, item, node.item)
    #     else:
    #         return node.item
