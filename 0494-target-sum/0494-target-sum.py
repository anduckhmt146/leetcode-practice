from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total - target) % 2 != 0 or total < target:
            return 0
        neg = (total - target) // 2
        
        # Init DP
        dp = [0] * (neg + 1)
        dp[0] = 1

        # Loop coin
        for num in nums:
            # Select only 1 => backward
            for i in range(neg, num - 1, -1):
                if i >= num:
                    dp[i] = dp[i] + dp[i - num]

        return dp[neg]
