from typing import List

class Solution:
    # Loop only in grid2
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            # If out of bounds or the cell is water, return immediately
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            
            # Mark the cell as visited by setting it to 0
            grid2[i][j] = 0
            
            # Initialize is_sub_island to True
            is_sub_island = True
            
            # Check if the current cell is a sub-island (must be land in grid1 as well)
            if grid1[i][j] == 0:
                is_sub_island = False
            
            # Visit all adjacent cells (up, down, left, right)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not dfs(x, y):
                    is_sub_island = False
            
            return is_sub_island

        sub_island_count = 0

        # Iterate over each cell in grid2
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    # If the entire island is a sub-island, increment the count
                    if dfs(i, j):
                        # Loop only 3 sub island in grid2
                        sub_island_count += 1

        return sub_island_count
