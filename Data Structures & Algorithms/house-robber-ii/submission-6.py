class Solution:
    def rob(self, nums: List[int]) -> int:
       # let dp be a tracker for total maximum you can rob
       # this is for the non-cyclic case; 
       n = len(nums)
       if n == 1:
        return nums[0]
       if n == 2:
        return max(nums[0], nums[1])

       #first case, exclude the first house 
       dp1 = [0]* (len(nums))
       dp1[0] = 0
       dp1[1] = nums[1]
       for i in range(2,len(nums)):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])

       #exclude final house 
       dp2 = [0]* len(nums)
       dp2[0] = nums[0]
       dp2[1] = max(nums[0], nums[1])
       for i in range(2, n-1):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
       return max(dp1[-1], dp2[n-2])