
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

from collections import defaultdict

class BoyerMoore:
    """"
    An efficient for substring search, Boyer Moore hops around like  bunny after building the first elements.
    """

    def __init__(self, needle):
        self.haystack = ""
        self.N = 0
        self.needle = needle
        self.M = len(needle)
        self.letterDict = defaultdict()
        for i,v in enumerate(needle):
            if i == self.M-1:
                self.letterDict[v] = self.M
            else:
                self.letterDict[v] = self.M - i - 1
            print(i, v, self.M - i - 1)
        print(self.letterDict)

    def search(self, haystack):
        self.N = len(haystack)
        assert(self.N > self.M)
        i,j = self.M, self.M
        # while i != self.N and j != self.N
        #     if 

x = BoyerMoore("team");
h = "there is no I in team bro"
print(len(h))
print(x.search(h))