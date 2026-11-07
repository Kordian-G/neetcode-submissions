class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0 
        n = len(nums)
        length = len(nums)+1

        for R in range(n):
            total += nums[R]

            while total >= target:
                length = min(R-L+1,length)
                total -= nums[L]
                L +=1

        if length == (len(nums)+1):
            return 0 
        else:
            return length

        