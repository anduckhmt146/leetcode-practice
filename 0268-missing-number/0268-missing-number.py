from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_pos = nums[i]
            # Place nums[i] at its correct position if possible
            # Also check that correct_pos < n to avoid index out of range since missing number is in 0..n
            if correct_pos < n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        # [9,6,4,2,3,5,7,0,1]
        # [0, 1, 2, 3, 4, 5, 6, 7, 9]
        print(nums)

        # After sorting, the first index where nums[i] != i is the missing number
        for i in range(n):
            if nums[i] != i:
                return i
        
        # If all numbers are at correct positions, then missing number is n
        return n
