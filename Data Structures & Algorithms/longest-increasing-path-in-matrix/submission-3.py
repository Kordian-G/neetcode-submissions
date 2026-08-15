class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}

        n_rows = len(matrix)
        n_columns = len(matrix[0])

        def dfs(i,j, prevval):
            if (i == n_rows or i<0 or
                j == n_columns or j<0 or
                matrix[i][j] <= prevval):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = 1
            res = max(res, 1+ dfs(1+i,j, matrix[i][j]))
            res = max(res, 1+ dfs(i,j+1, matrix[i][j]))
            res = max(res, 1+ dfs(i-1,j, matrix[i][j]))
            res = max(res, 1+ dfs(i,j-1, matrix[i][j]))
            dp[(i,j)] = res
            return res 

        for i in range(n_rows):
            for j in range(n_columns):
                dfs(i,j,-1)
        return max(dp.values())
