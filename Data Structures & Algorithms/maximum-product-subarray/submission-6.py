class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        Global_max = nums[0]
        Current_max = nums[0]
        Current_min = nums[0]

        for i in range(1, len(nums)):
            temp_max = Current_max
            Current_max = max(nums[i], temp_max * nums[i], Current_min *nums[i] )
            Current_min = min(nums[i], Current_min * nums[i], temp_max *nums[i] )
            Global_max = max(Global_max, Current_max)
        return Global_max