class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1

            while l<r:
                threesum= nums[i] + nums[l] +nums[r]
                if threesum >= target:
                    r-=1
                else:
                    res+=r-l 
                    l+=1
        return res

                        



        