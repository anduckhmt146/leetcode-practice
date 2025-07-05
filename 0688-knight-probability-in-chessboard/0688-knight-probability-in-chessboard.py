class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from functools import lru_cache

        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        @lru_cache(None)
        def dp(r, c, moves_left):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if moves_left == 0:
                return 1

            prob = 0
            for dr, dc in directions:
                prob += dp(r + dr, c + dc, moves_left - 1) / 8
            return prob

        return dp(row, column, k)
