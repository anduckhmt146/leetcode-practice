class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            # Check for out of bounds or water cells
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            # If the cell is already visited, return 0
            if visited[i][j]:
                return 0

            # Mark the cell as visited
            visited[i][j] = True

            # Recursively call dfs for adjacent cells and accumulate perimeter contributions
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)