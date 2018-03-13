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

        k = item[0]
        n_key = node.item[0]

        if k < n_key:
            node.left = self._put_helper(node.left, item)
        elif k > n_key:
            node.right = self._put_helper(node.right, item)
        else:
            node.item = item
        node.count = self._compute_size(node);
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
        if v < vo:
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
        if v > vo:
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

    def rank(self, item):
        return self._rankhelper(item, self.root)

    def _rankhelper(self, item, node):
        if node == None:
            return 0
        _, v = node.item
        _, vo = item
        if v < vo:
            return self._rankhelper(item, node.left)
        if v > vo:
            return 1 + self.size(node.left) + self._rankhelper(item, node.right)
        else:
            return self.size(node.left)

    def deleteMin(self):
        self._deleteminhelper(self.root)
    
    def _deleteminhelper(self, node):
        if node.left == None:
            return node.right
        node.left = self._deleteminhelper(node.left);
        node.count = self._compute_size(node)
        return node

    def delete(self, item):
        self._delete(self.root, item)
    
    def _delete(self, node, item):
        if node == None:
            return None
        _, v = node.item
        _, vo = item
        if v < vo:
            node.left = self._delete(node.left,item)
        elif v > vo:
            node.right = self._delete(node.right, item)
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


bst = BinarySearchTree();
bst.put((0,'a'))
bst.put((1,'c'))
bst.put((2,'j'))
print(bst.min_elem())
print(bst.max_elem())
bst.deleteMin()
print(bst.min_elem())
print(bst.rank((1,'c')))
print(bst.ceiling((2,'d')))
print(bst.floor((1,'d')))


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
