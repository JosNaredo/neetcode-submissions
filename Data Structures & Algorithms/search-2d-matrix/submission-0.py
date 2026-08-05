class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if target in line:
                return True
        else:
            return False