from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        num_rows, num_cols = len(board), len(board[0])
        visited = [[False] * num_cols for _ in range(num_rows)]

        # Handle edge case when the board only has one cell
        if num_rows == 1 and num_cols == 1 and board[0][0] == word:
            return True
        
        def get_neighbors(row, col):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    neighbors.append((r, c))
            
            return neighbors
        
        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or row >= num_rows or col < 0 or col >= num_cols or
                visited[row][col] or board[row][col] != word[index]):
                return False
            
            visited[row][col] = True
            
            for r, c in get_neighbors(row, col):
                if dfs(r, c, index + 1):
                    return True
            
            visited[row][col] = False  # Backtrack
            return False
        
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
