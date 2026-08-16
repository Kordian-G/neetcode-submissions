class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp is largest sum from subarrays ending at i 
        dp = [0] * n
        dp[-1] = nums[-1]

        for i in range(n-2,-1,-1):
            dp[i] = max(nums[i] , dp[i+1] + nums[i])
        return max(dp) 