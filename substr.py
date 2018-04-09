

from algorithms.substrsearch.kmp import KnuthMorrisPratt
from algorithms.substrsearch.boyermoore import BoyerMoore
import time

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


def shakespeare_test():
    "Test three way radix sort"
    with open('shakespeare.txt', mode='r') as f:
        shakespeare = f.read()
        boyerStart = time.time()
        b = BoyerMoore("thou")
        b.search(shakespeare)
        lenShake = len(shakespeare)
        boyerEnd = time.time()
        kmpStart = time.time()
        # kmp = KnuthMorrisPratt("thou")
        # kmp.search(shakespeare)
        kmpEnd = time.time()
        print(
            f"Boyer-Moore took #{boyerEnd - boyerStart} with #{lenShake} matches")
        print(f"KMP took #{kmpEnd - kmpStart }")

        # print(timeit.timeit(b.search(shakespeare)))
        # print(timeit.timeit(kmp.search(shakespeare)))


def basic_test():
    b = BoyerMoore("thou")
    x = b.search(""" His tender heir might bear his memory:
  But thou contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,""")

    print(b.matches)
    b = KnuthMorrisPratt("thou")
    x = b.search(""" His tender heir might bear his memory:
  But thou contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,""")
    print(b.matches)


# basic_test()
shakespeare_test()
