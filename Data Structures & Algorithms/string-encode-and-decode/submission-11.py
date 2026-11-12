class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string


    def decode(self, s: str) -> List[str]:
        l,r = 0,1
        words = []
        while l< len(s):
            r = l
            while s[r] != '#':
                r += 1
            digits = s[l:r]
            end = r + int(digits)
            word = s[r+1:end+1]
            words.append(word)
            l = end+1
        return words