class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array = [0] * len(arr)
        for i in range(len(arr) - 1):
            new_array[i] = max(arr[i+1:])
        new_array[-1] = -1
        return new_array




        