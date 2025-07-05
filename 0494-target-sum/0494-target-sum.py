from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # Check feasibility
        if (total - target) % 2 != 0 or total < target:
            return 0
        neg = (total - target) // 2
        
        # Initialize DP array
        dp = [0] * (neg + 1)
        dp[0] = 1  # There's one way to make sum 0: take nothing
        
        for num in nums:
            # Loop backwards to avoid using the same number multiple times
            for s in range(neg, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[neg]
