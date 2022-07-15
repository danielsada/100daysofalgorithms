"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
"""

import unittest
from typing import List

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __repr__(self) -> str:
        return f"[{self.start} - {self.end}]"
    
    def __eq__(self, o: object) -> bool:
        return self.start == o.start and self.end == o.end

def canAttendAllMeetings(intervals: List[Interval]) -> bool:
    intervals.sort(key=lambda x: x.start)
    for i in range(0, len(intervals)-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True
    
class ConflictTests(unittest.TestCase):
    def test_conflicts(self):
        self.assertFalse(canAttendAllMeetings([Interval(1,4), Interval(2,5), Interval(7,9)]))
        self.assertTrue(canAttendAllMeetings([Interval(6,7), Interval(2,4), Interval(8,12)]))
        self.assertFalse(canAttendAllMeetings([Interval(4,5), Interval(2,3), Interval(3,6)]))
