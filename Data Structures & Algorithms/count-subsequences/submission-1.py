class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # need two pointers i,j
        # dp stores number of distinct ways to store a subsequence from s to t 
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        # base case ( last column of dp is 1). to create "" target we need always 1 way
        # - choose nothing 
        for i in range(len(s)+1):
            dp[i][-1] = 1
        for i in range(len(s)-1,-1,-1):
            # at each step we have a choice to either include the 
            for j in range(len(t)-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                # if there is none, it's gotta be directly below 
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]


        