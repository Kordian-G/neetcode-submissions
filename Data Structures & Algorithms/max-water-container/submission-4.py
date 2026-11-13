class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        n = len(heights)
        l,r = 0, n-1
        vol = 0
        # right pointer will be moving one by one 
        # left pointer will be moving only if l+1 would contain more water
        def volume(l:str,r:str, array:list):
            return min(array[l],array[r])*(r-l)
        while l<r:
            vol = max(volume(l,r,heights),vol)
            if heights[l] <heights[r]:
                l+=1
            else:
                r-=1
        return vol
            





        
        