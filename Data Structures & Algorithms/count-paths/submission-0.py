class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # this is a quant question tho 
        number_of_ways = math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
        return number_of_ways