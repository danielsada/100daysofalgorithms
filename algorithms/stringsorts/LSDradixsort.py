
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class LSDRadixSort:
    """"
    A sort using the least significant digit which is proportional to lineal
    """

    def __init__(self, lsStrings, fixedLength):
        R = 256  # Assume ascii
        N = len(lsStrings)
        aux = [0]*(N+1)
        for d in range(fixedLength-1, -1, -1):
            count = [0]*(R+1)
            for i in range(0, N):
                count[ord(lsStrings[i][d]) + 1] += 1
            for r in range(0, R):
                count[r+1] += count[r]
            for i in range(0, N):
                aux[count[ord(lsStrings[i][d])]] = lsStrings[i]
                count[ord(lsStrings[i][d])] += 1
            for i in range(0, N):
                lsStrings[i] = aux[i]
        self.sorted = lsStrings
