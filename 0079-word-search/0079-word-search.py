from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge case: If the word is empty, it's trivially found
        if not word:
            return True
        
        num_rows, num_cols = len(board), len(board[0])

        # Function to get valid 4-directional neighbors
        def get_neighbors(row, col):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
    
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < num_rows and 0 <= c < num_cols:
                    neighbors.append((r, c))
            
            return neighbors

        # DFS function to find a path for the word
        def dfs(row, col, index):
            # Base case: If we've matched the entire word
            if index == len(word):
                return True

            # If out of bounds or character does not match, return False
            if board[row][col] != word[index]:
                return False

            # Mark the cell as visited by changing the character temporarily
            temp = board[row][col]
            board[row][col] = '#'

            # Explore neighbors
            for r, c in get_neighbors(row, col):
                if dfs(r, c, index + 1):
                    return True  # Found a match

            # Backtrack: restore the original character
            board[row][col] = temp
            return False

        # Handle edge case when the board only has one cell
        if num_rows == 1 and num_cols == 1 and board[0][0] == word:
            return True

        # Start DFS from each cell in the board
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == word[0]:  # Start DFS if the first character matches
                    if dfs(i, j, 0):  # Start DFS from position (i, j) with index 0
                        return True

        return False
