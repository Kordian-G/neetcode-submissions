class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in values:
                return sorted([i, nums.index(rem)])
            values[nums[i]] = i


             

        