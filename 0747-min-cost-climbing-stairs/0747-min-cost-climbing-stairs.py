from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # dp[i] = min cost to reach step i

        # Base cases
        dp[0] = 0  # start before step 0, no cost
        dp[1] = 0  # start before step 1, no cost

        for i in range(2, n + 1):
            dp[i] = min(
                dp[i-1] + cost[i-1],  # cost to come from one step below
                dp[i-2] + cost[i-2]   # cost to come from two steps below
            )

        return dp[n]
