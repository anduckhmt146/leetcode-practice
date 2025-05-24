from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(index: int, current_sum: int) -> int:
            # Base case: if at the end of array
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Check memo
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Choose '+'
            positive = backtrack(index + 1, current_sum + nums[index])
            # Choose '-'
            negative = backtrack(index + 1, current_sum - nums[index])

            memo[(index, current_sum)] = positive + negative
            return memo[(index, current_sum)]

        return backtrack(0, 0)
