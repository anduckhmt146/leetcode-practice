class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Init DP
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Step 2: Loop coin
        for coin in coins:
            # Step 3: Loop target
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
        