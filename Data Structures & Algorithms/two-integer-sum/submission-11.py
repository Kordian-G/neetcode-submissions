class Solution:

    # brute forced 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values =  {}
        for i,n in enumerate(nums):
            remainder = target - n
            if remainder in values:
                return [values[remainder], i]
            values[n] = i
             

        