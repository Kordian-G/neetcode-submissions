class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0 
        for l in range(len(arr)-k+1):
            r = min(l+k, len(arr))
            if ((sum(arr[l:r])/k) >= threshold) and l!=r:
                counter +=1
        return counter
            


        