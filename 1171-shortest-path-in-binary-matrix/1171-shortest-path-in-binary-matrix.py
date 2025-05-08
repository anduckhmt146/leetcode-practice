from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the starting or ending cell is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        # Directions for 8 possible moves (right, left, down, up, diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # BFS setup: queue stores (x, y, distance)
        queue = deque([(0, 0, 1)])  # Start from the top-left corner, with distance 1
        n = len(grid)  # Size of the grid
        
        # Mark the starting cell as visited
        grid[0][0] = 1
        
        while queue:
            x, y, dist = queue.popleft()
            
            # If we reach the bottom-right corner, return the distance
            if x == n - 1 and y == n - 1:
                return dist
            
            # Explore all 8 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds and not visited
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    # Mark the cell as visited
                    grid[nx][ny] = 1
                    # Add the new position to the queue with the incremented distance
                    queue.append((nx, ny, dist + 1))
        
        # If we finish BFS without reaching the bottom-right corner, return -1
        return -1
