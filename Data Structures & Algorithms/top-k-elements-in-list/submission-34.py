from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hasmap that counts each element
        c = Counter(nums)
        top_k = sorted(c.keys(),key = lambda x:c[x], reverse=True)[:k]
        return top_k
   