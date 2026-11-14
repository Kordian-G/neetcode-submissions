class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        starts = [0] * len(intervals)
        ends = [0] * len(intervals)
        for i, interval in enumerate(intervals):
            starts[i] = interval[0]
            ends[i] = interval[1]
        starts.sort()
        ends.sort()
        counter = 0
        answer = 0
        i, j=0,0
        while i < len(starts):
            if starts[i] <= ends[j]:
                counter+=1
                i+=1
            else:
                counter-=1
                j+=1
            answer= max(answer, counter)
        return answer

            

            

        
