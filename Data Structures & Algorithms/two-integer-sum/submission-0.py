class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #keep a set of subtracted values and compare to dictionary of values:
        # use a dictionary instead
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

                    