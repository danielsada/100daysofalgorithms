
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class MSDRadixSort:
    """
    A sort which performs well in cases where the start of
    the word is dissimilar.
    Most Significant Digit Radix Sort.
    """
    R = 256

    def __init__(self, lsStrings):
        self.n = len(lsStrings)
        self.aux = [0]*self.n
        self.sort(lsStrings, self.aux, 0, self.n-1, 0)
        self.sorted = lsStrings

    @staticmethod
    def charAt(string: str, pos: int) -> int:
        if pos == len(string):
            return -1
        else:
            return ord(string[pos])

    def sort(self, a, aux, lo, hi, d):
         # Assume ascii
        if hi <= lo:
            return
        count = [0]*(self.R+2)

        # frequency counts
        for i in range(lo, hi+1):
            c: int = self.charAt(a[i], d)
            count[c+2] += 1

        # counts to indices
        for r in range(0, self.R+1):
            count[r+1] += count[r]

        # distribute
        for i in range(lo, hi+1):
            c: int = self.charAt(a[i], d)
            aux[count[c+1]] = a[i]
            count[c+1] += 1

        # copy back
        for i in range(lo, hi+1):
            a[i] = aux[i - lo]

        for r in range(0, self.R+1):
            self.sort(a, aux, lo+count[r], lo + count[r+1]-1, d+1)
