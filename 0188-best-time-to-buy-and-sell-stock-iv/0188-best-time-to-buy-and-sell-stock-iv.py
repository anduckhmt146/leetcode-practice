from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Optimization for large k
        if k >= n // 2:
            return sum(
                max(prices[i] - prices[i - 1], 0) for i in range(1, n)
            )

        # dp[i][t][0 or 1]
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        for t in range(k + 1):
            dp[0][t][0] = 0
            dp[0][t][1] = -prices[0]  # if we buy on day 0

        for i in range(1, n):
            for t in range(1, k + 1):
                # Not holding
                dp[i][t][0] = max(dp[i-1][t][0], dp[i-1][t][1] + prices[i])
                # Holding
                dp[i][t][1] = max(dp[i-1][t][1], dp[i-1][t-1][0] - prices[i])

        return max(dp[n-1][t][0] for t in range(k + 1))  # max profit without holding
