import unittest


def get_all_subsets(input_arr):
    initial = [[]]



class TestSubsets(unittest.TestCase):
    def test_subset(self):
        input_arr = [1, 5, 3]
        result = [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]]


        # medianOfAStream = MedianOfAStream()
        # medianOfAStream.insert_num(3)
        # medianOfAStream.insert_num(1)
        # self.assertEqual(medianOfAStream.find_median(),2.0)
        # medianOfAStream.insert_num(5)
        # self.assertEqual(medianOfAStream.find_median(),3.0)
        # medianOfAStream.insert_num(4)
        # self.assertEqual(medianOfAStream.find_median(),3.5)

if __name__ == '__main__':
    unittest.main()