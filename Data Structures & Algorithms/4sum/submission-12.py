class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                # two sum at this point 
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l,r = j+1, n-1
                while l<r:
                    four_some = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_some < target:
                        l+=1
                    elif four_some >target:
                        r-=1
                    else:
                        t = (nums[i],nums[j],nums[l],nums[r])
                        res.append(t)
                        r-=1
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1] and r<n-1:
                            r -= 1
        return res


        