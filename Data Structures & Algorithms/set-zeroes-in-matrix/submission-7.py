class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, cols = [False]*len(matrix), [False]*len(matrix[0])        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i] = True
                    cols[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] or cols[j]:
                    matrix[i][j] = 0

        return