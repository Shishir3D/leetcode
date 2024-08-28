class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) -1
        l = 0

        while l <= r:
            m = (l+r)//2

            # if nums[m] == 5:
            #     print(5)    
            print(m)

            if len(nums) != 1 and nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m] < nums[m - 1]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return nums[0]



