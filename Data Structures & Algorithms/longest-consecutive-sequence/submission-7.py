class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sets = set(nums)
        maxim = 1
        for n in nums:
            length = 1
            if n-1 not in sets:
                while n+1 in sets:
                    n = n+1
                    length +=1 
                maxim = max(maxim,length)
        return maxim
                
                

