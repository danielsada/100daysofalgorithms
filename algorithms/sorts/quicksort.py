import random


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class QuickSort:
    """"
    Implementing quicksort
    """

    def __init__(self, arr, hasPlentyOfEqualElements=False):
        self.arr = arr
        random.shuffle(self.arr)
        if hasPlentyOfEqualElements:
            self.sorted = self.threeWayQuicksort(self.arr)
        else:
            self.sorted = self.quicksort(self.arr)

    # Thanks to gist by https://github.com/catovermoon

    def quicksort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)

    def threeWayQuicksort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        mid = [i for i in lst[1:] if i == pivot]
        less = [i for i in lst[1:] if i < pivot]
        greater = [i for i in lst[1:] if i > pivot]
        mid.append(pivot)
        return self.quicksort(less) + mid + self.quicksort(greater)
