class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        t = []
        for c in s:
            if c.isalnum():
                t.append(c.lower())
        l, r = 0, len(t) - 1
        while l <= r:
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True