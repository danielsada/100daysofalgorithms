"""
Subarrays with Product Less than a Target (medium)

Problem Statement

Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

from collections import deque
from itertools import product

def subarrays_product_less_than(input:list[int], target:int) -> list[list[int]]:
    left, product = 0, 1
    result = []
    for right in range(len(input)):
        product *= input[right]
        # if able, expand window
        while product >= target and left < len(input):
            product /= input[left]
            left += 1
        temporary = deque()
        for i in range(right, left-1, -1):
            temporary.appendleft(input[i])
            result.append(list(temporary))
    return result



import unittest

class testProduct(unittest.TestCase):
    def test_product(self):
        self.assertListEqual([[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]], subarrays_product_less_than([8, 2, 6, 5], 50))
        self.assertListEqual([[2], [5], [2, 5], [3], [5, 3], [10]], subarrays_product_less_than([2, 5, 3, 10], 30))