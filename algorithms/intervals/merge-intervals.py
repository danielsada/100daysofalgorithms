"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
"""

from typing import List
import unittest


class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __repr__(self) -> str:
        return f"[{self.start} - {self.end}]"
    
    def __eq__(self, __o: object) -> bool:
        return self.start == __o.start and self.end == __o.end

def merge(earlier_start: Interval, b: Interval):
    return Interval(earlier_start.start, max(earlier_start.end, b.end))

def merge_intervals(intervals: List[Interval]):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x.start)
    merged_intervals = []
    start, end = intervals[0].start, intervals[0].end
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        if current_interval.start <= end:
            end = max(end, current_interval.end)
        else:
            merged_intervals.append(Interval(start,end))
            start = current_interval.start
            end = current_interval.end
            
    merged_intervals.append(Interval(start,end))
    return merged_intervals

class TargetSumUt(unittest.TestCase):
    def test_examples(self):
        self.assertListEqual(merge_intervals([Interval(1,4), Interval(2,5), Interval(7,9)]), [Interval(1,5), Interval(7,9)])
        self.assertListEqual(merge_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]), [Interval(2,4), Interval(5,9)])
        self.assertListEqual(merge_intervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)]), [Interval(1,6)])

