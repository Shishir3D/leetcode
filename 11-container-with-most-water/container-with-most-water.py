class Solution:
    def maxArea(self, height: List[int]) -> int:
        # length = rpointer - lpointer -1
        # breadth = min(height[lpointer], height[rpointer])
        # current_area = length * breadth
        # max_area = max(current_area, max_area)

        lpointer = 0
        rpointer = len(height) - 1
        max_area = 0

        while lpointer < rpointer:
            length = rpointer - lpointer
            breadth = min(height[lpointer], height[rpointer])

            current_area = length * breadth
            max_area = max(current_area, max_area)

            if height[lpointer] < height[rpointer]:
                lpointer += 1
            else:
                rpointer -=1
        
        return max_area
