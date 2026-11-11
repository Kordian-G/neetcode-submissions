class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(image, r,c, original_color):
            # base cases
            ROWS = len(image)
            COLUMNS = len(image[0])
            if min(r,c)<0 or r>=ROWS or c>=COLUMNS or image[r][c] != original_color:
                return
        
            image[r][c] = color
            dfs(image,r+1,c, original_color)
            dfs(image,r,c+1, original_color)
            dfs(image,r-1,c, original_color)
            dfs(image,r,c-1, original_color)
        dfs(image,sr,sc, original_color)
        return image


            