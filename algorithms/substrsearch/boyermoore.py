
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

from collections import defaultdict
from re import match

# Trying to re-implement boyer moore more correctly
"""
class NewBoyerMoore:
    def __init__(self, text) -> None:
        self.text = text

    def get_matches(self, pattern):
        matches = []
        self.length_pattern = len(pattern)
        # When we start Boyer moore, we want to be in the end of the pattern
        # txt = ABCDEF
        # pattern = CD
        # A B C D E F
        #     C D
        # 0 1 2 3 4 5
#               |
#             |
        # set Initial position
        self.current_position = len(pattern) - 1
        # buffer is how many skips we have over the main text
        self.buffer = 0
        while self.current_position < len(self.text):
            for i in range(len(pattern)-1, 0, -1):
                print(self.text[self.buffer + i], pattern[i])
                if(i == 1):
                    #print("Found")
                if(self.text[self.buffer + i] != pattern[i]):
                    self.jump(1)
                    break
                #print("End")

        return matches
                     

    def jump(self, n):
        self.buffer += n
        self.current_position = self.buffer + self.length_pattern - 1

nb = NewBoyerMoore("Mary had a little lamb, little lamb")
print(nb.get_matches("lamb"))
"""

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
            # print(i, v, self.M - i - 1)
        # print(self.letterDict)

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


# x = BoyerMoore("teamtitans")
# h = "there is team no I in bro"
# f = x.search(h)
# print(f)
