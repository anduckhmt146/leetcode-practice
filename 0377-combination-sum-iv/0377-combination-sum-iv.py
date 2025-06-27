from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # There's one way to make 0 — choose nothing

        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]

        return dp[target]
