class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        storage = set()
        count_dup = 0
        for i in range(len(nums)):
            #check if they're duplicates
            if nums[i] not in storage:
                storage.add(nums[i])
            else:
                count_dup += 1
                nums[i] = float('inf')
        while float('inf') in nums:
            nums.remove(float('inf'))
        return len(nums)
