from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def count_ways(index: int, remaining: int) -> int:
            # Base cases
            if remaining == 0:
                return 1
            if index == len(coins):
                return 0

            # Check memo
            if (index, remaining) in memo:
                return memo[(index, remaining)]

            # Choose the coin
            pick = 0
            if coins[index] <= remaining:
                pick = count_ways(index, remaining - coins[index])
            # Skip the coin
            skip = count_ways(index + 1, remaining)

            memo[(index, remaining)] = pick + skip
            return memo[(index, remaining)]

        return count_ways(0, amount)
