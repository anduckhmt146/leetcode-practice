from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize the queue for BFS
        queue = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        
        # Enqueue all the rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        def bfs(queue: deque, fresh_oranges: int) -> int:
            # Directions for the 4-adjacency
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            minutes_elapsed = 0
            
            while queue and fresh_oranges > 0:
                minutes_elapsed += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            # This fresh orange now becomes rotten
                            grid[nx][ny] = 2
                            fresh_oranges -= 1
                            queue.append((nx, ny))
            
            return minutes_elapsed if fresh_oranges == 0 else -1
    
        return bfs(queue, fresh_oranges)
