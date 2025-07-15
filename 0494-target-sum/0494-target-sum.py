from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        target_sum = (total + target) // 2
        n = len(nums)

        # dp[i][j] = number of ways to reach sum j using first i numbers
        dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # One way to reach sum 0 with 0 elements

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target_sum + 1):
                if j < num:
                    dp[i][j] = dp[i - 1][j]  # can't pick num
                else:
                    # Pick num or skip it
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]

        return dp[n][target_sum]