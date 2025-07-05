class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # Knight moves from each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],         # 5 is unreachable by knight
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # dp[i][j]: number of ways to reach digit j at step i
        dp = [ [0] * 10 for _ in range(n) ]
        
        # Base case: 1 way to be at any digit at step 0
        for digit in range(10):
            dp[0][digit] = 1
        
        # Fill dp table
        for i in range(1, n):
            for digit in range(10):
                for nei in moves[digit]:
                    dp[i][digit] = (dp[i][digit] + dp[i - 1][nei]) % MOD
        
        return sum(dp[n - 1]) % MOD
