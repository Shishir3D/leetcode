class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        li = set()

        for num in nums:
            if num in li:
                return True
            else:
                li.add(num)
        return False