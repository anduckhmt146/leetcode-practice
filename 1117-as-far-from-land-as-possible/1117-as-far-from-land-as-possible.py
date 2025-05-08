from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        # Step 1: Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        # If there is no land or no water, return -1
        if not q or len(q) == n * n:
            return -1

        # Step 2: BFS from all land cells simultaneously
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = -1

        while q:
            distance += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If it's a water cell, mark it visited and add to queue
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 2  # Mark as visited
                        q.append((nx, ny))

        return distance
