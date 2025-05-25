from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        # Place each number at its correct index: nums[i] should be at nums[nums[i]-1]
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        # After placement, numbers which are not at correct index are missing
        disappeared = []
        for i in range(n):
            if nums[i] != i + 1:
                disappeared.append(i + 1)
        
        return disappeared
