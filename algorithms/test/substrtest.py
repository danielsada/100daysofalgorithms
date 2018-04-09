

import unittest
from algorithms.substrsearch.kmp import KnuthMorrisPratt
from algorithms.substrsearch.boyermoore import BoyerMoore
import timeit

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class SubStringTest(unittest.TestCase):
    def shakespeare_test(self):
        "Test three way radix sort"
        with open('shakespeare.txt', mode='r') as f:
            shakespeare = f.read()
            b = BoyerMoore("thou")
            kmp = KnuthMorrisPratt("thou")
            print(timeit.timeit(b.search(shakespeare)))
            print(timeit.timeit(kmp.search(shakespeare)))


if __name__ == '__main__':
    unittest.main()
