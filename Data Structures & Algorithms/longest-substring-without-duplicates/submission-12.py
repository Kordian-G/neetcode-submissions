class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sublist = []
        length = 0
        for R in range(len(s)):
            if s[R] in sublist:
                idx = sublist.index(s[R])
                sublist = sublist[idx + 1:]
            sublist.append(s[R])
            length = max(length, len(sublist))

        return length