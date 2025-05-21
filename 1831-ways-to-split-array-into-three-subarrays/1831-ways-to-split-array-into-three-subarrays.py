from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Compute prefix sum
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        result = 0

        # Step 2: Iterate over the first split point
        for i in range(n - 2):  # left ends at i
            left_sum = prefix[i]

            # Binary search for leftmost valid mid start (j)
            j = bisect_left(prefix, 2 * left_sum, i + 1, n - 1)

            # Binary search for rightmost valid mid end (k)
            k = bisect_right(prefix, (prefix[-1] + left_sum) // 2, j, n - 1)

            # Count valid mid ranges
            result += max(0, k - j)
            result %= MOD

        return result
