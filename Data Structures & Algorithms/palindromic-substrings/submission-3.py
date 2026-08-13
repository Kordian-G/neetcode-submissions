class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force 
        counter = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                if s[start:end] == s[end:start:-1]:
                    counter+=1
        return counter