class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for element in board:
            existing = []
            for sub_elemnt in element:
                if sub_elemnt in existing and sub_elemnt != '.':
                    return False
                else:
                    existing.append(sub_elemnt)
        for i in range(9):
            existing = []
            for j in range(9):
                if board[j][i] in existing and board[j][i] != '.':
                    return False
                else:
                    existing.append(board[j][i])
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                existing = []
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[j][i] in existing and board[j][i] != '.':
                            return False
                        else:
                            existing.append(board[j][i])

        return True

