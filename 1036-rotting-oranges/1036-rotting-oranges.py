from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # Step 1: Add all rotten oranges to the queue and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Step 2: BFS to rot adjacent fresh oranges
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
        minutes = 0

        while queue:
            r, c, mins = queue.popleft()
            minutes = max(minutes, mins)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the orange
                    fresh_oranges -= 1
                    queue.append((nr, nc, mins + 1))

        return minutes if fresh_oranges == 0 else -1
