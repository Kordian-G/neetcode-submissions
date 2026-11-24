from collections import Counter
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        while 0 in nums:
            nums.remove(0)

        number_of_0s = counter[0] 
        for i in range(number_of_0s):
            nums.append(0)
        



