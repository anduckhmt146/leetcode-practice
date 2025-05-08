from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = [[False] * cols for _ in range(rows)]
        borders = []

        def dfs(r, c):
            visited[r][c] = True
            is_border = False
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                # Logic check border, and we only want to color original_color
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != original_color:
                    is_border = True
                elif not visited[nr][nc]:
                    dfs(nr, nc)
            if is_border:
                borders.append((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid
