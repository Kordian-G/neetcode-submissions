class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum_area = 0
        stack = [] 
        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                curr_area = height*(i - idx)
                maximum_area = max(curr_area, maximum_area)
                start= idx
            stack.append((start,h))

        for idx, height in stack:
            maximum_area = max(maximum_area, height* (len(heights)-idx))
        return maximum_area

        