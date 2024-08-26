class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # find the row where the target resides
        while top <= bottom:
            middle = (top + bottom) // 2
            mm = matrix[middle]
            if target >= mm[0] and target <= mm[-1]:
                break
            elif target > mm[-1]:
                top = middle + 1
            elif target < mm[0]:
                bottom = middle - 1

        #finds the target value
        l = 0
        r = len(mm) -1

        while l <= r:
            m = (l + r) // 2

            if target == mm[m]:
                return True
            elif target > mm[m]:
                l = m + 1
            elif target < mm[m]:
                 r = m - 1
        
        return False



        
        