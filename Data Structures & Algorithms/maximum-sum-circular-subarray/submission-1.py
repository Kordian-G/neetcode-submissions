from itertools import permutations
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #kadane's algo should help 
        # this is standard but now need to account for different
        arrays = []
        for i in range(len(nums)):
            arrays.append(nums[i:] + nums[:i])
        maxarray_sum = []
        for arr in arrays:
            maxSum = arr[0]
            currSum = 0
            for n in arr:
                currSum = max(0, currSum)
                currSum += n 
                maxSum = max(currSum, maxSum)
            maxarray_sum.append(maxSum)
        return max(maxarray_sum)

        