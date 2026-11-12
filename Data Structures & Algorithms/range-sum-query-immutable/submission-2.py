class NumArray:

    def __init__(self, nums: List[int]):
        self.array = []
        total = 0
        for n in nums:
            total +=n
            self.array.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preright = self.array[right]
        preleft = self.array[left-1] if left>0 else 0
        return (preright - preleft)

        
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)