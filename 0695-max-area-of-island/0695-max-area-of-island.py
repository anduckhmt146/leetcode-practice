from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        # Flip 1 to 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # mark as visited

            # When first DFS, count it
            area = 1
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                area += dfs(r + dr, c + dc)
            
            # Area each time count DFS
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea
