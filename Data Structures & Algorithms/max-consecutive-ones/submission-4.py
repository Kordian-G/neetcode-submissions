class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        counting = []
        for num in nums:
            if (num == 1):
                counter += 1
            else:
                counting.append(counter)
                counter = 0
        counting.append(counter)
        return max(counting) 

            
        