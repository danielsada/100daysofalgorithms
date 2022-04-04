"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
"""

from nis import match
import unittest


def sliding_window_find_permutations(input :str, pattern :str) -> bool:
    pattern_hash_map = {}
    window_start, matches = 0, 0
    for pos in range(len(pattern)):
        if pattern[pos] in pattern_hash_map:
            pattern_hash_map[pattern[pos]] += 1
        else:
            pattern_hash_map[pattern[pos]] = 1
    
    for window_end in range(len(input)):
        right_char = input[window_end]
        if right_char in pattern_hash_map:
            pattern_hash_map[right_char] -= 1
            if pattern_hash_map[right_char] == 0:
                matches += 1
        if matches == len(pattern_hash_map):
            return True;
        if window_end >= len(pattern) -1:
            left_char = input[window_start]
            window_start += 1
            if left_char in pattern_hash_map:
                if pattern_hash_map[left_char] == 0:
                    matches -= 1
                pattern_hash_map[left_char] += 1
    return False
             
import unittest

class sliding_unittests(unittest.TestCase):
    def test_sliding_case1(self):
        self.assertTrue(sliding_window_find_permutations("oidbcaf","abc"))
        self.assertFalse(sliding_window_find_permutations("odicf","dc"))
        self.assertTrue(sliding_window_find_permutations("bcdxabcdy","bcdyabcxd"))
        self.assertTrue(sliding_window_find_permutations("aaacb", "abc"))

        

