class Solution:
    def longestPalindrome(self, s: str) -> str:
        # perhaps try and split string s into substrings of increasing
        # length.
        palindromes = []
        for start in range(len(s)):
            for end in range(start +1,len(s)+1):
                substring = s[start:end]
                if substring == substring[::-1]:
                    palindromes.append(substring)
        
        return max(palindromes, key=len)

                    

            
            
        