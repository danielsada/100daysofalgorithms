import unittest


def get_all_subsets(input_arr):
    subset = []
    subset.append([])
    for nums in input_arr:
        n = len(subset)
        for i in range(n):
            set1 = list(subset[i])
            set1.append(nums)
            subset.append(set1)
    return subset
    


class TestSubsets(unittest.TestCase):
    def test_subset(self):
        input_arr = [1, 5, 3]
        result = [[], [1], [5],[1,5], [3], [1,3], [5,3], [1,5,3]]
        self.assertListEqual(get_all_subsets(input_arr), result)

if __name__ == '__main__':
    unittest.main()