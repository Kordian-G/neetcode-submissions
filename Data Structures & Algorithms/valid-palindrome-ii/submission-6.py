class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            # while l<r and not s[l].isnum():
            #     l+=1
            # while l<r and not s[r].isnum():
            #     r-=1
            if s[l] != s[r]:
                skipl = s[l+1: r+1]
                skipr = s[l:r]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
            l, r = l+1, r-1
        return True
    