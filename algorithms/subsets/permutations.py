from collections import deque
from itertools import permutations
import unittest


def get_all_permutations(numbers):
    return permutations(numbers)

def get_all_permutations_bfs(numbers):
    pass



class TestSubsets(unittest.TestCase):
    def test_subset(self):
        input_arr = [1, 5, 3]
        result = [(1,3,5), (1,5,3), (3,1,5), (3,5,1), (5,1,3), (5,3,1)]
        self.assertCountEqual(list(get_all_permutations(input_arr)), result)
        self.assertCountEqual(list(get_all_permutations_bfs(input_arr)), result)

if __name__ == '__main__':
    unittest.main()