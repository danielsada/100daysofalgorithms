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

    def put(self, item: tuple):
        self.root = self._put_helper(self.root, item)

    def _put_helper(self, node: BSTNode,  item: tuple) -> BSTNode:
        if node == None:
            return BSTNode(item)

        k = item[0]
        n_key = node.item[0]

        if k < n_key:
            node.left = self._put_helper(node.left, item)
        elif k > n_key:
            node.right = self._put_helper(node.right, item)
        else:
            node.item = item
        sz_node_right = self.size(node.right) if self.size(
            node.right) != None else 0
        sz_node_left = self.size(node.left) if self.size(
            node.left) != None else 0
        node.count = 1 + sz_node_left + sz_node_right
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

    def max_elem(self):
        elem = self.root
        while elem != None and elem.right != None:
            elem = elem.right
        return elem.item

    def min_elem(self):
        elem = self.root
        while elem != None and elem.left != None:
            elem = elem.left
        return elem.item

    def floor(self, item):
        x = self._floorhelper(self.root, item)
        if x == None:
            return None
        return x.item

    def _floorhelper(self, node, item):
        if node == None:
            return None
        _, v = node.item
        _, vo = item
        if v == vo:
            return node
        if vo < v:
            return self._floorhelper(node.left, item)
        t = self._floorhelper(node.right, item)
        if t != None:
            return t
        else:
            return node

    def ceiling(self, item):
        x = self._ceilinghelper(self.root, item)
        if x == None:
            return None
        return x.item

    def _ceilinghelper(self, node, item):
        if node == None:
            return None
        _, v = node.item
        _, vo = item
        if v == vo:
            return node
        if vo < v:
            t = self._ceilinghelper(node.right, item)
            if t != None:
                return t
            else:
                return node
        return self._ceilinghelper(node.right, item)

    def size(self, node=None):
        if node == None:
            return self.root.count
        return node.count

    def iterable(self, key) -> iter:
        pass


# Alternative solution for floor:
    # def floor(self, item):
    #     if item == None:
    #         return None
    #     return self._floorhelper(self.root, item, None)

    # def _floorhelper(self, node, item, best):
    #     if node == None:
    #         return best
    #     _, v = node.item
    #     _, vo = item
    #     if vo < v:
    #         return self._floorhelper(node.left, item, best)
    #     elif vo > v:
    #         return self._floorhelper(node.right, item, node.item)
    #     else:
    #         return node.item
