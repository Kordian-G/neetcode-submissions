class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        hmap = {'}':'{', ']':'[',')':'('}
        for char in s:
            if char in'({[':
                stack.append(char)
            else:
                if  not stack or hmap[char] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0  


        