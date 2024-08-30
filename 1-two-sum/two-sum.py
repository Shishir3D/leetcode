class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        
        for index, num in enumerate(nums):
            mapp[num] = index
        print(mapp)
        for index, num in enumerate(nums):
            diff = target - num
            if (diff) in mapp and mapp[diff] != index:
                return [index, mapp[diff]]

