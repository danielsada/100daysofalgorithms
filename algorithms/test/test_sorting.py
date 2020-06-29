import unittest
from algorithms.sorts.selectionsort import SelectionSort
from algorithms.sorts.mergesort import MergeSort
from algorithms.sorts.insertionsort import InsertionSort
from algorithms.sorts.shellsort import ShellSort
from algorithms.sorts.quicksort import QuickSort


__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Tests for sorting arrays.
"""


class SortingTest(unittest.TestCase):
    def setUp(self):
        self.big_arr = [55, 59, 44, 68, 22, 78, 83, 23, 50, 66, 100, 71, 40, 47, 31, 70, 64, 11, 20, 90, 32, 75, 33, 35, 52, 4, 18, 73, 79, 84, 29, 54, 45, 77, 28, 5, 69, 39, 3, 60, 6, 93, 12, 62, 86, 7, 57, 81,
                        74, 13, 38, 43, 1, 25, 15, 37, 30, 85, 92, 24, 58, 16, 34, 21, 95, 51, 82, 88, 67, 98, 41, 14, 80, 94, 17, 76, 56, 63, 72, 97, 42, 10, 61, 89, 26, 87, 36, 96, 91, 19, 8, 53, 46, 9, 49, 27, 48, 65, 2, 99]
        self.big_arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                               50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
        self.negNums = [-1, -123124213, 0, -0,  -23, -1312, -41234]
        self.negNumsSorted = [-123124213, -41234, -1312, -23, -1, -0, 0]

    def test_selection_sort(self):
        selsort = SelectionSort(self.big_arr)
        self.assertEqual(selsort.sorted, self.big_arr_sorted)
        selsort = SelectionSort([])
        self.assertEqual(selsort.sorted, [])
        selsort = SelectionSort(self.negNums)
        self.assertEqual(selsort.sorted, self.negNumsSorted)

    def test_merge_sort(self):
        mergesort = MergeSort(self.big_arr)
        self.assertEqual(mergesort.sorted, self.big_arr_sorted)
        mergesort = MergeSort([])
        self.assertEqual(mergesort.sorted, [])
        mergesort = MergeSort(self.negNums)
        self.assertEqual(mergesort.sorted, self.negNumsSorted)

    def test_insertion_sort(self):
        insertionSort = InsertionSort(self.big_arr)
        self.assertEqual(insertionSort.sorted, self.big_arr_sorted)
        insertionSort = InsertionSort([])
        self.assertEqual(insertionSort.sorted, [])
        insertionSort = InsertionSort(self.negNums)
        self.assertEqual(insertionSort.sorted, self.negNumsSorted)

    def test_shell_sort(self):
        shellsort = ShellSort(self.big_arr)
        self.assertEqual(shellsort.sorted, self.big_arr_sorted)
        shellsort = ShellSort([])
        self.assertEqual(shellsort.sorted, [])
        shellsort = ShellSort(self.negNums)
        self.assertEqual(shellsort.sorted, self.negNumsSorted)

    def test_quick_sort(self):
        quicksort = QuickSort(self.big_arr)
        self.assertEqual(quicksort.sorted, self.big_arr_sorted)
        quicksort = QuickSort([])
        self.assertEqual(quicksort.sorted, [])
        quicksort = QuickSort(self.negNums)
        self.assertEqual(quicksort.sorted, self.negNumsSorted)

    def test_three_way_quick_sort(self):
        quicksort = QuickSort(self.big_arr, True)
        self.assertEqual(quicksort.sorted, self.big_arr_sorted)
        quicksort = QuickSort([], True)
        self.assertEqual(quicksort.sorted, [])
        quicksort = QuickSort(self.negNums, True)
        self.assertEqual(quicksort.sorted, self.negNumsSorted)


if __name__ == '__main__':
    unittest.main()
