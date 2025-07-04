class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n + 1):
            dp[i] = (0 if i == n else cost[i]) + min(dp[i - 1], dp[i - 2])

        return dp[n]

        