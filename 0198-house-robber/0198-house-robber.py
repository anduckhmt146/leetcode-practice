class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Find max -> init 0
        # dp is max value the thief can get until the home i
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # dp[i - 1] là skip nhà ith
            # dp[i - 2] + nums[i] là lấy nhà i - 2 và i
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]
        