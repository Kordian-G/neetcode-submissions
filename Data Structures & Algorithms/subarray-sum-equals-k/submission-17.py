class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        seen = defaultdict(int)
        seen[0] = 1   
        for n in nums:
            total += n
            count += seen[total - k] 
            seen[total] += 1 

        return count