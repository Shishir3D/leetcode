class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0
        longest_sequence = 0

        for nums in num_set:
            if nums -1 not in num_set:
                pos = 1
                current_sequence = 1

                while nums + 1 in num_set:
                    current_sequence += 1
                    nums += 1

                longest_sequence = max(current_sequence, longest_sequence) 
        
        return longest_sequence
            

