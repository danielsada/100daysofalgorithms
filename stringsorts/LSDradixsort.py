
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
        aux = [None]*N
        for d in range(fixedLength-1, 0, -1):
            count = []*(R+1)
            for i in range(0, N):
                count[ord(lsStrings[i][d]) + 1] += 1
            for r in range(0, R):
                count[r+1] = count[r]
            for i in range(0, N):
                aux[count[ord(lsStrings[i][d])]] = lsStrings[i]
                count[ord(lsStrings[i][d])] += 1
            for i in range(0, N):
                lsStrings[i] = aux[i]
