class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = []
        for i in nums:
            if i in unique_nums:
                return True
            else:
                unique_nums.append(i)
        return False
            
        