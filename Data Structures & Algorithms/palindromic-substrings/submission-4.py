class Solution:
    def countSubstrings(self, s: str) -> int:
    # there might be an edge case for len(s) = 1; 
    # firstly, let's use those two pointers and DP solution 
        palindrome_count_odd = 0
        for i in range(len(s)):
            # intiialize pointers 
            l,r = i,i 
            while l>=0 and r < len(s) and s[l] == s[r]:
                palindrome_count_odd += 1
                l -=1
                r +=1
        palindrome_count_even = 0
        for i in range(len(s)):
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] ==s[r]:
                palindrome_count_even +=1
                l -= 1
                r += 1
        return palindrome_count_even+ palindrome_count_odd



        