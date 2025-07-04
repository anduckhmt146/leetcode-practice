class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Step 1: DP
        dp = [[0] * (n + 1) for _ in range(m + 1)] 

        # Step 2: Coin
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            # Step 3: Target
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]        