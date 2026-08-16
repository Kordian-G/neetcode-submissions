class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp is the length of the maximum strictly increasing subsequence starting at i 
        dp = [1]* (len(nums))
        dp[-1] = 1
        n = len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]: 
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

        