from typing import List

class Solution:
    def coinChange(self, coins, amount):
        if amount <= 0 or not coins:
            return 0

        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        # If amount is 0, we need 0 coins
        for i in range(n):
            dp[i][0] = 0

        # Initialize the first row: use only the first coin
        for a in range(1, amount + 1):
            if a % coins[0] == 0:
                dp[0][a] = a // coins[0]

        # Process all sub-problems
        for i in range(1, n):
            for a in range(1, amount + 1):
                countWithI = float('inf')
                if coins[i] <= a:
                    countWithI = 1 + dp[i][a - coins[i]]
                countWithoutI = dp[i - 1][a]
                dp[i][a] = min(countWithI, countWithoutI)

        result = dp[n - 1][amount]
        return result if result != float('inf') else -1

