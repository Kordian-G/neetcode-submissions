from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hasmap that counts each element
        c = Counter(nums)
    
        heap = []
        for i in c:
            pair = (c[i],i)
            heapq.heappush(heap, pair)
            if len(heap)>k:
                heapq.heappop(heap)
        lst = [ pair[1] for pair in heap]
        return lst
            