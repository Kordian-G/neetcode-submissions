class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for duplicates in a given row:
        for r in range(9):
            seen = set()
            for i in range(9):
                if board[r][i] != "." and board[r][i] in seen :
                    return False
                seen.add(board[r][i])
        
        for c in range(9):
            seen= set() 
            for r in range(9):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square//3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] != "." and board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True


        
                



        