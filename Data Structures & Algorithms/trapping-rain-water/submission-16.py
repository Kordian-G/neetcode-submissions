class Solution:
    def trap(self, height: List[int]) -> int:
        #create an array with water hieghts; then sum
        height_so_far_left = height[0]
        height_so_far_right = height[-1]

        water_left =  [0] * len(height)
        water_right =  [0] * len(height)
        water_right[len(height)-1] = 0
        water = 0  
        for i in range(1, len(height)):
            height_so_far_left = max(height_so_far_left, height[i])       
            if height[i] < height_so_far_left:
                water_left[i] = height_so_far_left - height[i]

        for i in range(len(height)-2,-1,-1):
            height_so_far_right = max(height_so_far_right, height[i])       
            if height[i] < height_so_far_right:
                water_right[i] = height_so_far_right - height[i]       
        # now going backwards to make sure there are no gaps
        for i in range(len(height)):
            water+= min(water_left[i],water_right[i])
        return water

        
