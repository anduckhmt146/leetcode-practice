from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        result = []
        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        return result
