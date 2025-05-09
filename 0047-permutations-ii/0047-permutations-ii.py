from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort to group duplicates together

        def backtrack(nums, i):
            if i == len(nums):
                result.append(nums)
                return

            used = set()
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue  # Skip duplicates at this level

                used.add(nums[j])
                new_nums = nums[:]  # make a copy
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
                backtrack(new_nums, i + 1)

        backtrack(nums, 0)
        return result
