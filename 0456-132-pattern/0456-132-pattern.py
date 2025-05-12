from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # This will store potential "2"s (nums[k]) in decreasing order
        third = float('-inf')  # This keeps track of the "2" in the 132 pattern

        # Traverse from right to left
        # Next greater element
        # Next
        for num in reversed(nums):
            if num < third:
                # Found a 132 pattern
                return True
            # Greater
            while stack and stack[-1] < num:
                # Pop all smaller elements and update the "2" (third)
                third = stack.pop()
            stack.append(num)

        return False
