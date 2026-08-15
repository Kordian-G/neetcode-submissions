class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #1. Initialize a dp array:
        dp = [[0] * 2 for _ in range(len(prices) + 2)]
        #Bottom-Down approach:
        for i in range(len(prices)-1, -1,-1):
            dp[i][0] = max(dp[i+1][1] - prices[i], dp[i+1][0])
            dp[i][1] = max(dp[i+2][0] + prices[i], dp[i+1][1])
        return dp[0][0]
