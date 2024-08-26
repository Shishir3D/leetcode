class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for each in matrix:
            if target in each:
                return True
        return False
        