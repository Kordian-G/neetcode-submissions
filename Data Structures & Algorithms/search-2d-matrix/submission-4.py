class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full_array = []

        for row in matrix:
            for value in row:
                full_array.append(value)
        #then binary search on this unpacked array:
        l,r = 0, len(full_array)-1
        while l <=r:
            mid = (l+r)//2
            if target< full_array[mid]:
                r= mid - 1
            elif target > full_array[mid]:
                l = mid +1
            else:
                return True
        return False



        