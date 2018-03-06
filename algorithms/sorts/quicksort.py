import random


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class QuickSort:
    """"
    Implementing quicksort
    """

    def __init__(self, arr):
        self.arr = arr
        random.shuffle(self.arr)
        self.sorted = self.quicksort(self.arr)

    # Thanks to gist by https://github.com/catovermoon

    def quicksort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)
