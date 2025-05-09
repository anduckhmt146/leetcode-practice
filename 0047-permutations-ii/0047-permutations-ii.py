from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort to make it easy to skip duplicates

        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
                return

            # [1,2], [1,3], [1,4]
            # When the i = 1 is pass, i = 2 and continue
            seen = set()  # Used to skip duplicates at this recursion level
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

        backtrack()
        return result
