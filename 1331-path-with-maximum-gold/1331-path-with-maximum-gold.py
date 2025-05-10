from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x: int, y: int) -> int:
            gold = grid[x][y]
            grid[x][y] = 0  # mark as visited

            # NOTES: TOTAL RESULT AFTER BACKTRACKING
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                    max_gold = max(max_gold, dfs(nx, ny))

            grid[x][y] = gold  # backtrack
            return gold + max_gold

        max_total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    max_total = max(max_total, dfs(i, j))

        return max_total
