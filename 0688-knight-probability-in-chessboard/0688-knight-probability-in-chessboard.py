class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        # dp[m][r][c] = probability of being on cell (r, c) after m moves
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1  # Start at (row, column)

        for m in range(1, k + 1):         # 1️⃣ For each move from 1 to k
            for r in range(n):           # 2️⃣ For each row on the board
                for c in range(n):       # 3️⃣ For each column on the board
                    for dr, dc in directions:  # 4️⃣ For each possible knight move
                            prev_r, prev_c = r - dr, c - dc
                            if 0 <= prev_r < n and 0 <= prev_c < n:
                                dp[m][r][c] += dp[m - 1][prev_r][prev_c] / 8

        # Sum up all probabilities of being on the board after k moves
        total_prob = sum(dp[k][r][c] for r in range(n) for c in range(n))
        return total_prob
