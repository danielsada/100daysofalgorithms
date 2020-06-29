
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class ThreeWayRadixSort:
    """"
    Implementing radix sort for long common prefixes
    Bently and Sedgewick (1997)
    """

    @staticmethod
    def charAt(string: str, pos: int) -> int:
        if pos == len(string):
            return -1
        else:
            return ord(string[pos])

    def __init__(self, stringls):
        self.stringls = stringls
        self.sorted = self.threeWayQuicksort(self.stringls, 0)

    def threeWayQuicksort(self, lst, d):
        if len(lst) <= 1:
            return lst
        pivot = self.charAt(lst[0], d)
        mid = [i for i in lst if self.charAt(i, d) == pivot]
        less = [i for i in lst if self.charAt(i, d) < pivot]
        greater = [i for i in lst if self.charAt(i, d) > pivot]
        return self.threeWayQuicksort(less, d) + self.threeWayQuicksort(mid, d+1) + self.threeWayQuicksort(greater, d)
