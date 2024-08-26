class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # find the row where the number resides
        while top <= bottom:
            middle = (top + bottom) // 2
            mm = matrix[middle]
            if target >= mm[0] and target <= mm[-1]:
                break
            elif target > mm[-1]:
                top = middle + 1
            elif target < mm[0]:
                bottom = middle - 1

        if target in mm:
            return True
        return False

        # l = 0
        # r = len(mm) -1

        # while l <= r:



        
        