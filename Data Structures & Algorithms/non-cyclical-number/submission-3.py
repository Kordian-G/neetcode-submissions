class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            string = str(n)
            for i in range(len(string)):
                s += int(string[i])**2
            n = s
        return n == 1