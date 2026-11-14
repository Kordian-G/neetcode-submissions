from collections import defaultdict
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        answer = 0

        latest_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= latest_end:
                latest_end = end
            else:
                answer+=1
                latest_end = min(latest_end, end)
        return answer




        