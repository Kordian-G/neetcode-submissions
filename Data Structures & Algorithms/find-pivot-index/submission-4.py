class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # create prefix sums:
        total_sum = []
        total = 0 
        for n in nums:
            total += n
            total_sum.append(total)
        
        for i in range(len(nums)):
            pre_on_left = total_sum[i-1] if i>0 else 0 
            pre_on_right = total_sum[-1] - total_sum[i]
            if pre_on_left == pre_on_right:
                return i
        return -1