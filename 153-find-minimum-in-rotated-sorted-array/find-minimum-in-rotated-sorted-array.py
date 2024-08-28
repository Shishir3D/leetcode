class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        for num in nums:
            if num < low:
                low = num
        
        return low