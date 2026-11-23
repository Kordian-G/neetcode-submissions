class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        storage = set()
        for i in range(len(nums1)):
            if nums1[i] not in storage:
                storage.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in storage and nums2[i] not in res:
                res.append(nums2[i])
        return res

        