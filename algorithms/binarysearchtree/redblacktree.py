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

    def _rotate_left(self, node: RBTNode):
        assert self.isRed(node.right)
        child_node:RBTNode = node.right
        node.right = child_node.left
        child_node.left = node
        child_node.color = node.color
        node.color = self.RED
        return child_node
    
    def  _rotate_right(self, node:RBTNode):
        assert self.isRed(node.left)
        child_node : RBTNode = node.left
        node.left = child_node.right
        child_node.right = node
        child_node.color = node.color
        node.color = self.RED
        return child_node

    def _flip_colors(self, node:RBTNode):
        assert not self.isRed(node)
        assert self.isRed(node.right)
        assert self.isRed(node.left)
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    def put(self, item: tuple):
        self.root = self._put_helper(self.root, item)
        self.root.color = self.BLACK

    def _put_helper(self, node: RBTNode,  item: tuple) -> RBTNode:
        if node == None:
            return RBTNode(item, RBT.RED)
        xk,_ = node.item
        k,_ = item
        if k < xk:
            node.left = self._put_helper(node.left, item)
        elif k > xk:
            node.right = self._put_helper(node.right, item)
        else:
            node.item = item
        
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self._rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self._rotate_right(node)
        if self.isRed(node.left) and self.isRed(node.right):
            node = self._flip_colors(node)
        
        return node
        
    def delete(self, key):
        assert key != None
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = self.RED
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, h:RBTNode, key):
        hk,_ = h
        if key < hk:
            if not self.isRed(h.left) and not self.isRed(h.left.left):
                h = self._moveRedLeft(h)
            h.left = self._delete_helper(h.left, key)
        else:
            if self.isRed(h.left):
                h = self._rotate_right(h)
            if key == hk and h.right == None:
                return None
            if not self.isRed(h.right) and not self.isRed(h.right.left):
                h = self._moveRedRight(h)
            if key == hk:
                x : RBTNode = self.minimum(h.right)
                h.item = x.item
                h.right = self.delete_minimum(h.right)
            else:
                h.right = self._delete_helper(h.right, key)
        return self._balance(h)

    def _moveRedLeft(self, node):
        assert node != None
        assert self.isRed(node) and not self.isRed(node.left) and not self.isRed(node.left.left)
        node = self._flip_colors(node)
        if not self.isRed(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            node = self._flip_colors(node)
        return node

    def _moveRedRight(self, node):
        assert node != None
        assert self.isRed(node) and not self.isRed(node.right) and not self.isRed(node.right.left)
        node = self._flip_colors(node)
        if self.isRed(node.left.left):
            node = self._rotate_right(node)
            node = self._flip_colors(node)
        return node
    
    def minimum(self, node):
        if node.left == None:
            return node
        else:
            return node.left

    def delete_minimum(self, node):
        if node.left == None:
            return None
        if self.isRed(node.left) and not self.isRed(node.left.left):
            node = self._moveRedLeft(node)
        node.left = self.delete_minimum(node.left)
        return self._balance(node)


    def _balance(self, node):
        if self.isRed(node.right):
            node = self._rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self._rotate_right(node)
        if self.isRed(node.left) and self.isRed(node.right):
            node = self._flip_colors(node)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node
        

    def size(self, node):
        if node == None or node.count == None:
            return 0
        return node.count

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

   