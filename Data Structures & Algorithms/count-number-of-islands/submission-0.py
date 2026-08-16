class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        counter = 0
        
        def dfs(r, c):
            # Base Case: Out of bounds OR reached water ("0")
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            # Sink the island cell (mark as visited)
            grid[r][c] = "0"
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Main Scan
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i, j) # Sink the entire connected island
                    
        return counter