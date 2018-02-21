
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Implementation of basic Heap Methods in python
"""


class Heap:
    def __init__(self):
        self.size = 0
        self.elements = []

    @staticmethod
    def left_index(parentIndex):
        return 2*parentIndex + 1

    @staticmethod
    def right_index(parentIndex):
        return 2*parentIndex + 2

    @staticmethod
    def parent_index(childIndex):
        return (childIndex-1)/2

    def has_right_index(self, parentIndex):
        return (self.right_index(parentIndex) > self.size)

    def has_left_index(self, parentIndex):
        return (self.left_index(parentIndex) < self.size)

    def has_parent(self, childIndex):
        return (self.parent_index(childIndex) >= 0)

    def value_right(self, parentIndex):
        return self.elements[self.right_index(parentIndex)]

    def value_left(self, parentIndex):
        return self.elements[self.left_index(parentIndex)]

    def value_parent(self, childIndex):
        return self.elements[self.parent_index(childIndex)]

    def swap(self, i, j):
        temp = self.elements[i]
        self.elements[i] = self.elements[j]
        self.elements[j] = temp
