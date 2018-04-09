
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

from collections import defaultdict


class BoyerMoore:
    """"
    An efficient for substring search, Boyer Moore hops around like  bunny after building the first elements.
    """

    def __init__(self, needle):
        self.matches = []
        self.haystack = ""
        self.N = 0
        self.needle = needle
        self.M = len(needle)
        self.letterDict = defaultdict()
        for i, v in enumerate(needle):
            if i == self.M-1:
                self.letterDict[v] = self.M
            else:
                self.letterDict[v] = self.M - i - 1
            print(i, v, self.M - i - 1)
        print(self.letterDict)

    def search(self, haystack):
        self.N = len(haystack)
        assert(self.N > self.M)
        # Conventions, nI is needle iterator,
        # hI is a haystack iterator
        # cI is a comparison iterator
        nI, hI = self.M-1, self.M-1
        while hI < self.N:
            nI = self.M - 1
            letters = 0
            cI = hI
            while(haystack[cI].lower() == self.needle[nI].lower() and letters < self.M):
                nI -= 1
                cI -= 1
                letters += 1
            if letters == self.M:
                self.matches.append((haystack[hI-self.M+1:hI+1], hI-self.M))
                hI += 1
                continue
            else:
                if self.letterDict.__contains__(haystack[hI]):
                    hI += self.letterDict[haystack[hI]]
                else:
                    hI += self.M-1
        return None


# x = BoyerMoore("team")
# h = "there is no I in bro"
# print(len(h))
# index = x.search(h)
# print(index)
