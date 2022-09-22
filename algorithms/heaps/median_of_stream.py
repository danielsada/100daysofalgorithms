"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""
from multiprocessing import heap
import unittest
import heapq

class MedianOfAStream:
    minHeapEnd = []
    maxHeapStart = []

    def insert_num(self, num):
        if self.maxHeapStart and -self.maxHeapStart[0] >= num:
            heapq.heappush(self.maxHeapStart, -num)
        else:
            heapq.heappush(self.minHeapEnd, num)
        
        lenmin = len(self.maxHeapStart)
        lenmax = len(self.minHeapEnd)
        
        if lenmax > lenmin + 1:
            heapq.heappush(self.maxHeapStart, -heapq.heappop(self.minHeapEnd))
        elif lenmax < lenmin:
            heapq.heappush(self.minHeapEnd, -heapq.heappop(self.maxHeapStart))        
        
    def find_median(self):
        if len(self.maxHeapStart) == len(self.minHeapEnd):
            return ((-self.maxHeapStart[0]) + self.minHeapEnd[0])/2.0
        else:
            return self.minHeapEnd[0]


class TestMedian(unittest.TestCase):
    def test_median(self):
        medianOfAStream = MedianOfAStream()
        medianOfAStream.insert_num(3)
        medianOfAStream.insert_num(1)
        self.assertEqual(medianOfAStream.find_median(),2.0)
        medianOfAStream.insert_num(5)
        self.assertEqual(medianOfAStream.find_median(),3.0)
        medianOfAStream.insert_num(4)
        self.assertEqual(medianOfAStream.find_median(),3.5)

if __name__ == '__main__':
    unittest.main()