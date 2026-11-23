class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        n = len(nums)

        for i in range(n):
            l,r= i+1, n-1
            while l<r:
                if nums[r] + nums[i] + nums[l] >0:
                    r-=1
                elif nums[r] + nums[i] + nums[l] <0:
                    l+=1
                else:
                    if sorted([nums[i],nums[l],nums[r]]) not in res:
                        res.append(sorted([nums[i],nums[l],nums[r]]))
                    l+=1
                    r-=1
        return res 
                    


            
        