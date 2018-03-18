
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class ShellSort:
    """"
    Creating a class that implements selection sort
    """

    def __init__(self, arr):
        self.arr = arr
        self.shellSort()
        self.sorted = arr

    def shellSort(self):
        h = 1
        while h < len(self.arr)/3:
            h = 3*h + 1
        while h >= 1:
            i = 0
            while i < len(self.arr):
                for j in range(i, 0, -h):
                    if j != 0:
                        if self.arr[j-h] > self.arr[j]:
                            self.swap(j, j-h)
                i += 1
            h = h // 3

    def swap(self, i, j):
        if not(i < 0 or j < 0):
            self.arr[i] ^= self.arr[j]
            self.arr[j] ^= self.arr[i]
            self.arr[i] ^= self.arr[j]
