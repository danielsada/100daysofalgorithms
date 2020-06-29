
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


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
        self.dfa[ord(self.needle[0])][0] = 1
        x = 0
        for j in range(1, self.M):
            for c in range(0, self.R):
                self.dfa[c][j] = self.dfa[c][x]
            self.dfa[ord(self.needle[j])][j] = j+1
            x = self.dfa[ord(self.needle[j])][x]

    def search(self, haystack):
        self.N = len(haystack)
        curr = 0
        while haystack != '':
            curr = self._kmp(haystack)
            self.matches.append(curr)
            haystack = haystack[curr+self.M:]

    def _kmp(self, arr):
        N = len(arr)
        i, j = 0, 0
        while i < N and j < self.M:
            j = self.dfa[ord(arr[i])][j]
            i += 1
        if j == self.M:
            return i-self.M
        else:
            return N
