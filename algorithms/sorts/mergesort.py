
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class MergeSort:
    """"
    Uses and applies MergeSort
    """

    def __init__(self, arrToSort):
        self.sorted = self.mergeSort(arrToSort)

    @staticmethod
    def merge(left, right):
        if left is None or len(left) == 0:  # pylint: disable=C1801
            return right
        if right is None or len(right) == 0:  # pylint: disable=C1801
            return left
        res = []
        i = 0
        j = 0
        while len(res) < len(left) + len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
            if i == len(left):
                res.extend(right[j:])
            if j == len(right):
                res.extend(left[i:])
        return res

    def mergeSort(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr)//2
        lf = self.mergeSort(arr[0:mid])
        rg = self.mergeSort(arr[mid:len(arr)])
        return self.merge(lf, rg)
