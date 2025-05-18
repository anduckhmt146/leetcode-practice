from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count = 0
        prev_count = 0
        start = -1

        for i, num in enumerate(nums):
            # num > right (invalid)
            if num > right:
                start = i
                prev_count = 0
            # left <= num <= right
            elif num >= left:
                prev_count = i - start
                count += prev_count
            # num < left
            else:
                count += prev_count

        return count
