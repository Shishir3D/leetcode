from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers at the start and end of the array
        left_pointer = 0
        right_pointer = len(nums) - 1

        # Loop continues until the search range is exhausted
        while left_pointer <= right_pointer:
            # Calculate the middle index to divide the search space in half
            mid_pointer = left_pointer + (right_pointer - left_pointer) // 2

            # Get the values at the left, right, and mid pointers for clarity
            left_value = nums[left_pointer]
            right_value = nums[right_pointer]
            mid_value = nums[mid_pointer]

            # Check if the middle value is the target
            if mid_value == target:
                return mid_pointer  # Found the target, return its index

            # Determine if the left half is sorted
            if left_value <= mid_value:
                # If the target is within the range of the sorted left half
                if left_value <= target < mid_value:
                    # Move the right pointer to the left to search within the sorted left half
                    right_pointer = mid_pointer - 1
                else:
                    # Otherwise, move the left pointer to the right to search in the unsorted right half
                    left_pointer = mid_pointer + 1
            else:
                # If the left half isn't sorted, then the right half must be sorted
                if mid_value < target <= right_value:
                    # If the target is within the range of the sorted right half
                    # Move the left pointer to the right to search within the sorted right half
                    left_pointer = mid_pointer + 1
                else:
                    # Otherwise, move the right pointer to the left to search in the unsorted left half
                    right_pointer = mid_pointer - 1

        # If the loop ends, the target is not in the array
        return -1
