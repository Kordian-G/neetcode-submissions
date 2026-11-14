"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x: x.start)
        answer = 0
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        i,j =0,0
        counter = 0
        while i < len(intervals):
            if starts[i] < ends[j]:
                counter+=1
                i+=1
            else:
                counter-=1
                j+=1
            answer = max(answer,counter)
        return answer
            

        