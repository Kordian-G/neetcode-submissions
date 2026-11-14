class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort 
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        output = []
        previous_interval = [] # start
        for interval in sorted_intervals:
            if not previous_interval or interval[0] > previous_interval[1]:
                previous_interval = interval
                output.append(previous_interval)
            elif interval[0] <= previous_interval[1]:
                previous_interval = [previous_interval[0], interval[1]] if interval[1] > previous_interval[1] else [previous_interval[0], previous_interval[1]]
                output[-1]=previous_interval
        return output

        