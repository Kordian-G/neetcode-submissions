"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key= lambda x: x.start)

        latest_interval = intervals[0]
        for interval in intervals[1:]:
            if interval.start < latest_interval.end:
                return False
            else:
                latest_interval = interval
        return True
