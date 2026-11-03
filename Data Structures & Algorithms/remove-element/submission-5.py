class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue 
            tmp.append(num)
        for j in range(len(tmp)):
            nums[j] = tmp[j]
        return len(tmp) 

        