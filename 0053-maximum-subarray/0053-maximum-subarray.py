from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current max and global max to the first element
        current_sum = max_sum = nums[0]

        # Iterate through the rest of the array
        for num in nums[1:]:
            # Either start new subarray at current num or extend previous one
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
