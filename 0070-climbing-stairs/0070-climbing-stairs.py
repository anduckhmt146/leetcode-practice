class Solution:
    def climbStairs(self, n: int) -> int:
        # To go to the step i => go 1 step from step i - 1 or go 2 steps from i - 2
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]        