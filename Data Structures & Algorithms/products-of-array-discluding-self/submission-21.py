class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_left,pre_right= 1,1
        left,right = [],[]
        for i in range(len(nums)):
            left.append(pre_left)
            pre_left *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            right.append(pre_right)
            pre_right *=nums[i]
        right.reverse()
        res = []
        for i in range(len(nums)):
            prod = right[i] *left[i]
            res.append(prod)
        return res
            
