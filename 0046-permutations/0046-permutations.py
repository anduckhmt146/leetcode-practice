from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, i):
            if i == len(nums):
                result.append(nums)
                return
            for j in range(i, len(nums)):
                new_nums = nums[:]            # make a fresh copy
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
                backtrack(new_nums, i + 1)

        backtrack(nums, 0)
        return result
