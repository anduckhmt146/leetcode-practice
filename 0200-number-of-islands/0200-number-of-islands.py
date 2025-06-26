class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        countNumIslands = 0

        def isValid(row_index, col_index):
            return 0 <= row_index < row and 0 <= col_index < col and not visited[row_index][col_index]

        
        def dfs(row_index, col_index):
            if not isValid(row_index, col_index) or grid[row_index][col_index] == "0":
                return
            
            # Visited it
            grid[row_index][col_index] = "0" 
            visited[row_index][col_index] = True

            # DFS without backtrack
            dfs(row_index + 1, col_index)
            dfs(row_index - 1, col_index)
            dfs(row_index, col_index + 1)
            dfs(row_index, col_index - 1)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    if isValid(i, j):
                        dfs(i, j)
                        countNumIslands += 1

        return countNumIslands
