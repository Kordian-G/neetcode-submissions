class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.original_table = matrix
        self.sum_table = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        # create each row array sum 
        for i in range(len(matrix)):
            total = 0
            for j in range(len(matrix[0])):
                total += matrix[i][j]
                self.sum_table[i][j] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row_sums = []
        for row in range(row1,row2+1):
            row_sum_right = self.sum_table[row][col2]
            row_sum_left = self.sum_table[row][col1-1] if col1>0 else 0 
            row_sum = row_sum_right - row_sum_left
            row_sums.append(row_sum)
        return sum(row_sums)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
