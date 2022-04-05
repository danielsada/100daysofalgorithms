"""
Maximum Sum Subarray of Size K (easy)

Problem Statement

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def maximum_sum_subarray(input:list[int], k:int) -> int:
    window_start, maxsum, current_sum = 0, 0, 0
    for window_end in range(len(input)):
        if window_end - window_start - k == 0:
            current_sum += input[window_end]
            current_sum -= input[window_start]
            window_start += 1
        else:
            current_sum += input[window_end]
        maxsum = max(maxsum, current_sum)
    return maxsum        

import unittest

class SumKUnitTests(unittest.TestCase):
    def test_sumk(self):
        self.assertEqual(maximum_sum_subarray([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(maximum_sum_subarray([2, 3, 4, 1, 5], 2), 7)
