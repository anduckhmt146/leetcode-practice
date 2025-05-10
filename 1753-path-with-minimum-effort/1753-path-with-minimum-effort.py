import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        min_heap = [(0, 0, 0)]  # (effort, x, y)

        while min_heap:
            curr_effort, x, y = heapq.heappop(min_heap)
            if x == rows - 1 and y == cols - 1:
                return curr_effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    next_effort = max(curr_effort, abs(heights[nx][ny] - heights[x][y]))
                    if next_effort < effort[nx][ny]:
                        effort[nx][ny] = next_effort
                        heapq.heappush(min_heap, (next_effort, nx, ny))

        return 0  # fallback (shouldn't be reached)
