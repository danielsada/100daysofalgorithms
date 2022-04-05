"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

def target_sum(input:list[int], target:int) -> list[int]:
    p1, p2 = 0, len(input)-1
    for i in range(len(input)): # lazy way to garantee the program finishes
        if p1 >= p2:
            return []
        if input[p1] + input[p2] > target:
            p2 -= 1
        elif input[p1] + input[p2] < target:
            p1 += 1
        else:
            return [p1, p2]

import unittest

class TargetSumUt(unittest.TestCase):
    def test_examples(self):
        self.assertListEqual(target_sum([2, 5, 9, 11], 11), [0,2])
        self.assertListEqual(target_sum([1, 2, 3, 4, 6], 6), [1,3])
