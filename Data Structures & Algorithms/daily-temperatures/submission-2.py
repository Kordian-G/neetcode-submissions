class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]* len(temperatures)
        stack = [] 
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_t, stack_indx = stack.pop()
                output[stack_indx] = (i - stack_indx)
            stack.append([temperature, i])
        return output

            