
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class KnuthMorrisPratt:
    """"
    An efficient for substring search, Knuth Morris Pratt builds a DFA based on the matching pattern
    """
    R = 256

    def __init__(self, needle):
        self.matches = []
        self.haystack = ""
        self.N = 0
        self.needle = needle
        self.M = len(needle)
        self.dfa = [[0 for x in range(self.M)] for y in range(self.R)]
        # print(self.dfa)
        # print(self.needle[0])
        self.dfa[ord(self.needle[0])][0] = 1
        x = 0
        for j in range(1, self.M):
            for c in range(0, self.R):
                self.dfa[c][j] = self.dfa[c][x]
            self.dfa[ord(self.needle[j])][j] = j+1
            x = self.dfa[ord(self.needle[j])][x]

    def search(self, haystack):
        self.haystack = haystack
        current = 0
        self.N = len(self.haystack)
        while current < self.N:
            current = self._kmp(current)
            self.matches.append(current)

    def _kmp(self, i=0):
        j = 0
        while i < self.N and j < self.M:
            print(self.haystack[i], end=" ",)
            j = self.dfa[ord(self.haystack[i])][j]
            i += 1
        if j == self.M:
            return i-self.M
        else:
            return self.N
