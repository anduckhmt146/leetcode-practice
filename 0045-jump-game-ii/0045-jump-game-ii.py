from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n  # Initialize dp array with ∞
        dp[0] = 0  # No jumps needed to reach the first index

        # Loop through every index from 1 to n-1
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:  # Can we jump from j to i?
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]
