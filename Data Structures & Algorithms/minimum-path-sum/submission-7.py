class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # initialize dp with padding:
        dp = [[float('inf')] * (COLUMNS+1) for _ in range(ROWS+1)]
        # base case 
        dp[ROWS][COLUMNS-1] = 0 
        for i in range(ROWS-1, -1,-1):
            for j in range(COLUMNS-1,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


        