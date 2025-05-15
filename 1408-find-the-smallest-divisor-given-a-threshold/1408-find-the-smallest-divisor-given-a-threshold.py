from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Helper to compute the total sum of ceil divisions
        def compute_sum(divisor: int) -> int:
            return sum((num + divisor - 1) // divisor for num in nums)

        # Binary search range: 1 to max(nums)
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
