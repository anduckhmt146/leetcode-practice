from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                if i != correct_pos:
                    # Duplicate found
                    return nums[i]
                else:
                    i += 1
        return -1  # If no duplicate found (problem guarantees one duplicate)
