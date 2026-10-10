class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        top_k = [num for num,freq in counts.most_common(k)]
        return top_k