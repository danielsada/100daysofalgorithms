
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class SelectionSort:
    """"
    We are sorting elements with selection sort.
    """

    def __init__(self, arr):
        self.arr = arr
        self.selection_sort()

    def selection_sort(self):
        index = 0
        while index != len(self.arr) + 1:
            sz = len(self.arr)
            if self.arr[index+1:] != []:
                sw_index = self.arr.index(min(self.arr[index+1:]))
                if self.arr[sw_index] < self.arr[index]:
                    self.swap(index, sw_index)
                index += 1
            else:
                break

    def swap(self, i, j):
        self.arr[i] ^= self.arr[j]
        self.arr[j] ^= self.arr[i]
        self.arr[i] ^= self.arr[j]


v = SelectionSort([0, 2, 1, 69, 3, 9])
print(v.arr)
