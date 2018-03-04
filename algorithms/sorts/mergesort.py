
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class MergeSort:
    """"
    Uses and applies MergeSort
    """

    def __init__(self, arrToSort):
        self.sorted = self.merge_sort(arrToSort)

    def merge(self, left, right):
        if left == None or len(left) == 0:
            return right
        if right == None or len(right) == 0:
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

    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr)//2
        lf = self.merge_sort(arr[0:mid])
        rg = self.merge_sort(arr[mid:len(arr)])
        return self.merge(lf, rg)


x = MergeSort([2, 3, 4, 1, 5, 8])
print("Teoretically ", x.sorted)
