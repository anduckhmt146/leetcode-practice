class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            # Mark the visited land
            grid[i][j] = 0
            
            # Start with the current land cell
            area = 1
            
            # Accumulate area from all adjacent cells (up, down, left, right)
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            
            return area

        max_area = 0
        
        # Iterate over each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(current_area, max_area)
        
        return max_area
