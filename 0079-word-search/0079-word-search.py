from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or board[r][c] != word[i]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            
            # Flip the word[i] to '#' is found
            board[r][c] = "#"
            
            # Explore neighbors in 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                found = dfs(r + dr, c + dc, i + 1)  # Recursively check neighbors
                if found:
                    return True
            
            # Restore the cell
            board[r][c] = temp
            
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
