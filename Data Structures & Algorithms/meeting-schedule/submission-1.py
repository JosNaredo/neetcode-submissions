"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = sorted(intervals, key=lambda x: x.start)
        for i in range(len(res)-1):
            if res[i].end > res[i+1].start:
                return False

        
        return True