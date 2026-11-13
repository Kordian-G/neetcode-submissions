class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers

        n = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(n):
            if nums[i] == nums[i-1] and i>0:
                continue
            r,l = n-1, i+1
            while l<r:
                if nums[r] +nums[l] +  nums[i] <0:
                    l+=1
                elif nums[r] +nums[l] +  nums[i] >0:
                    r-=1
                else:
                    if sorted([nums[i],nums[r],nums[l]]) not in res:
                        res.append(sorted([nums[i],nums[r],nums[l]])) 
                    l+=1
                    r-=1       
        return res
   
        