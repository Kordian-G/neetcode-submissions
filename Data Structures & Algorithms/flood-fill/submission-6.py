class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original_color = image[sr][sc]

        def dfs(image, r,c, values, original_color):
            # base cases
            ROWS = len(image)
            COLUMNS = len(image[0])
            if min(r,c)<0 or r>=ROWS or c>=COLUMNS or (r,c) in values or image[r][c] != original_color:
                return
        
            image[r][c] = color
            values.add((r,c))

            dfs(image,r+1,c, values, original_color)
            dfs(image,r,c+1, values, original_color)
            dfs(image,r-1,c, values, original_color)
            dfs(image,r,c-1, values, original_color)
        dfs(image,sr,sc, set(), original_color)
        return image


            