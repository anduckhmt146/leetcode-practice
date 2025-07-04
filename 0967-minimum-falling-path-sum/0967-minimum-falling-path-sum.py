from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Start from the second-last row and go upward
        for row in range(n - 2, -1, -1):
            for col in range(n):
                # Get values from the next row: directly below, left-diagonal, right-diagonal
                down = matrix[row + 1][col]
                left = matrix[row + 1][col - 1] if col > 0 else float('inf')
                right = matrix[row + 1][col + 1] if col < n - 1 else float('inf')
                
                # Update current cell with min falling path sum
                matrix[row][col] += min(down, left, right)

        # The answer is the min in the first row
        return min(matrix[0])
