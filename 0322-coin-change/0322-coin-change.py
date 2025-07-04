class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Loop coin
        # Step 2: Loop target
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # Base case


        # amount + 1 => Because to reach amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


