class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Find dp sum with nums / 2
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target] != 0

        