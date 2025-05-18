from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Move left forward if nums[left] is even
            if nums[left] % 2 == 0:
                left += 1
            # Move right backward if nums[right] is odd
            elif nums[right] % 2 == 1:
                right -= 1
            # If nums[left] is odd and nums[right] is even, swap them
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums
