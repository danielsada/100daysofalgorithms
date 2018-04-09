from algorithms.substrsearch.kmp import KnuthMorrisPratt
from algorithms.substrsearch.boyermoore import BoyerMoore
import time
import re
import unittest

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class SubStrTest(unittest.TestCase):
    def test_shakespeare(self):
        "Test three way radix sort"
        with open('shakespeare.txt', mode='r') as f:
            shakespeare = f.read()
            boyerStart = time.time()
            b = BoyerMoore("thou")
            b.search(shakespeare)
            lenShake = len(b.matches)
            boyerEnd = time.time()
            pyStart = time.time()
            thous = [m for m in re.findall("thou", shakespeare.lower())]
            lenPy = len(thous)
            pyEnd = time.time()
            kmpStart = time.time()
            kmp = KnuthMorrisPratt("thou")
            kmp.search(shakespeare.lower())
            lenKMP = len(kmp.matches)
            kmpEnd = time.time()
            print(
                f"Boyer took #{boyerEnd - boyerStart} with #{lenShake} matches")
            print(f"Find took #{pyEnd - pyStart } with #{lenPy} matches")
            print(f"KMP took {kmpEnd-kmpStart} with #{lenKMP} matches")
            self.assertEqual(lenPy, lenShake+1, lenKMP-1)

    def test_basic_substr(self):
        bm = BoyerMoore("thou")
        bm.search(""" His tender heir might bear his memory:
    But thou contracted to thine own bright eyes,
    Feed'st thy light's flame with self-substantial fuel,
    Making a famine where abundance lies,
    Thy self thy foe, to thy sweet self too cruel:
    Thou that art now the world's fresh ornament,
    And only herald to the gaudy spring,
    Within thine own bud buriest thy content,""")

        print(bm.matches)
        kmp = KnuthMorrisPratt("thou")
        kmp.search(""" His tender heir might bear his memory:
    But thou contracted to thine own bright eyes,
    Feed'st thy light's flame with self-substantial fuel,
    Making a famine where abundance lies,
    Thy self thy foe, to thy sweet self too cruel:
    Thou that art now the world's fresh ornament,
    And only herald to the gaudy spring,
    Within thine own bud buriest thy content,""".lower())
        print(kmp.matches)
        self.assertEqual(len(kmp.matches)-1, len(bm.matches))


if __name__ == '__main__':
    unittest.main()
