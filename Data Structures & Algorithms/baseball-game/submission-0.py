class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array_score = [] 
        for op in operations:
            if op == "D":
                array_score.append(array_score[-1]*2)
            elif op == "C":
                array_score.pop()
            elif op == "+":
                array_score.append(array_score[-1]+array_score[-2])
            else:
                array_score.append(int(op))
        return sum(array_score)


        