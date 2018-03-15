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

    def _inorderhelper(self, node: BSTNode):
        if node == None:
            return
        self._inorderhelper(node.left)
        self.inorder_arr.append(node.item)
        self._inorderhelper(node.right)

    def put(self, item: tuple):
        self.root = self._put_helper(self.root, item)

    def _put_helper(self, node: BSTNode,  item: tuple) -> BSTNode:
        if node == None:
            return BSTNode(item)
        k,_ = item
        xk,_ = node.item
        if k < xk:
            node.left = self._put_helper(node.left, item)
        elif k > xk:
            node.right = self._put_helper(node.right, item)
        else:
            node.item = item
        node.count = 1 + self.size(node.left) + self.size(node.right)
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

    def floor(self, key):
        x = self._floorhelper(self.root, key)
        if x == None:
            return None
        return x.item

    def _floorhelper(self, node, key):
        if node == None:
            return None
        xk,_ = node.item
        if xk == key:
            return node
        if key < xk:
            return self._floorhelper(node.left, key)
        t = self._floorhelper(node.right, key)
        if t != None:
            return t
        else:
            return node

    def ceiling(self, key):
        x = self._ceilinghelper(self.root, key)
        if x == None:
            return None
        return x.item

    def _ceilinghelper(self, node, key):
        if node == None:
            return None
        xk,_ = node.item
        if xk == key:
            return node
        if key < xk:
            t = self._ceilinghelper(node.right, key)
            if t != None:
                return t
            else:
                return node
        return self._ceilinghelper(node.right, key)

    def size(self, node):
        if node == None or node.count == None:
            return 0
        return node.count

    def size_at_root(self):
        return  self.size(self.root);           


    def deleteMin(self):
        self.root = self._deleteminhelper(self.root)
    
    def _deleteminhelper(self, node):
        if node.left == None:
            return node.right
        node.left = self._deleteminhelper(node.left);
        node.count = self._compute_size(node)
        return node

    def delete(self, key):
        self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node == None:
            return None
        xk,_ = node.item
        
        if key < xk:
            node.left = self._delete(node.left,key)
        elif key > xk:
            node.right = self._delete(node.right, key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            tempNode = node
            node = self._minelemfromNode(tempNode.right)
            node.right = self._deleteminhelper(node)
            node.left = tempNode.left
        node.count = self._compute_size(node)
        return node
    
        
    def _minelemfromNode(self, node):
        if node.left == None: 
            return node
        else:
            return self._minelemfromNode(node.left)
            

    def _compute_size(self, node):
        sz_node_right = self.size(node.right) if self.size(
            node.right) != None else 0
        sz_node_left = self.size(node.left) if self.size(
            node.left) != None else 0
        return 1 + sz_node_left + sz_node_right




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
