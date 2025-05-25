from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        
        while i < n:
            correct_pos = nums[i] - 1
            # Place nums[i] at its correct position if possible
            if 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        # After placement, the first index where nums[i] != i+1 is the missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers are in correct place, missing positive is n+1
        return n + 1
