
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class InsertionSort:
    """
    Creating a class that implements selection sort
    """

    def __init__(self, arr):
        self.arr = arr
        self.insertionSort()
        self.sorted = self.arr

    def insertionSort(self):
        i = 0
        while i < len(self.arr):
            for j in range(i, 0, -1):
                if j != 0:
                    if self.arr[j-1] > self.arr[j]:
                        self.swap(j, j-1)
            i += 1

    def swap(self, i, j):
        self.arr[i] ^= self.arr[j]
        self.arr[j] ^= self.arr[i]
        self.arr[i] ^= self.arr[j]
