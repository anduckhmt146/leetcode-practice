class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[i] = min number of steps to get i 'A's

        for i in range(2, n + 1):
            dp[i] = i  # worst case: all Paste after one Copy All at 1
            for j in range(i // 2, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break  # we want the largest factor to minimize steps

        return dp[n]
