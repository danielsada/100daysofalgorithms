import unittest
from algorithms.stringsorts.LSDradixsort import LSDRadixSort
from algorithms.stringsorts.MSDradixsort import MSDRadixSort
from algorithms.stringsorts.threewayradixsort import ThreeWayRadixSort


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class StringSortTest(unittest.TestCase):
    def setUp(self):
        self.length6 = ["oyflpu", "zdeuqi", "gbhorm", "hoyvzp",
                        "wxkdfe", "lachzc", "ihxeed", "xfnnlk", "avzuot",
                        "srwukx", "fpgwnb", "dymhgo", "atonur", "aecbmy",
                        "cbbkst", "upgthf", "hfjsxy", "iffcnv", "bbfknq", "uyrpsp"]
        self.length3 = ["cfg", "uks", "nbw", "doj", "frm", "nru", "rte", "tqa", "gge",
                        "lpk", "ypf", "ozz", "mwq", "qiw", "vfh", "yab", "lxf", "vwm", "tzh", "ecu"]
        self.length1 = ["x", "m", "y", "w", "q", "l", "e", "i", "o",
                        "v", "d", "j", "k", "g", "t", "u", "b", "n", "s", "r"]
        self.slength6 = sorted(self.length6)
        self.slength3 = sorted(self.length3)
        self.slength1 = sorted(self.length1)

    def test_lsd_radix_sort(self):
        "Test lsd radix sort with lenght 6, 3 & 1"
        a = LSDRadixSort(self.length6, 6)
        b = LSDRadixSort(self.length3, 3)
        c = LSDRadixSort(self.length1, 1)
        self.assertEqual(a.sorted, self.slength6)
        self.assertEqual(b.sorted, self.slength3)
        self.assertEqual(c.sorted, self.slength1)

    def test_msd_radix_sort(self):
        "Test msd radix sort"
        a = MSDRadixSort(self.length6)
        b = MSDRadixSort(self.length3)
        c = MSDRadixSort(self.length1)
        self.assertEqual(a.sorted, self.slength6)
        self.assertEqual(b.sorted, self.slength3)
        self.assertEqual(c.sorted, self.slength1)

    def test_3way_radix_sort(self):
        "Test three way radix sort"
        a = ThreeWayRadixSort(self.length6)
        b = ThreeWayRadixSort(self.length3)
        c = ThreeWayRadixSort(self.length1)
        self.assertEqual(a.sorted, self.slength6)
        self.assertEqual(b.sorted, self.slength3)
        self.assertEqual(c.sorted, self.slength1)


if __name__ == '__main__':
    unittest.main()
