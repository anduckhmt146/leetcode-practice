from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If total sum is odd, can't partition equally
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # dp[i][j] = True if subset of first i numbers can make sum j
        dp = [[False] * (target + 1) for _ in range(n)]

        # Sum 0 is always possible: take no elements
        for i in range(n):
            dp[i][0] = True

        # With only the first number, can we form sum nums[0]?
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # Process all subsets
        for i in range(1, n):
            for j in range(1, target + 1):
                # Exclude current number
                dp[i][j] = dp[i - 1][j]

                # Include current number if it does not exceed the sum
                if nums[i] <= j:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i]]

        return dp[n - 1][target]
