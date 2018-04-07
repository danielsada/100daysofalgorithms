
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class KnuthMorrisPratt:
    """"
    An efficient for substring search, Knuth Morris Pratt builds a DFA based on the matching pattern
    """
    R = 256
    def __init__(self, needle):
        self.haystack = "";
        self.N = 0;
        self.needle = needle
        self.M = len(needle)
        self.dfa = [[0 for x in range(self.R)] for y in range(self.M)] 
        self.dfa[self.needle[0]][0] = 1
        x = 0
        for j in range (1, self.M):
            for c in range (0, self.R):
                self.dfa[c][j] = self.dfa[c][x]
            self.dfa[self.needle[j]][j] = j+1;
            x = self.dfa[self.needle[j]][x];


    def search(self, haystack):
        self.haystack = haystack
        self.N = len(haystack)
        i, j = 0,0
        while i < self.N and j < self.M:
            j = self.dfa[self.haystack[i]][j]
            i+=1
        if j==self.M: 
            return i-self.M;
        else:
            return self.N
