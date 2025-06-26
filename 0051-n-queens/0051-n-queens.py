class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []

        def isValid(row_index, col_index):
            # Check col
            for i in range(n):
                if board[i][col_index] == 'Q':
                    return False
            
            # Check upper-left diagonal (Only check upper row)
            i, j = row_index - 1, col_index - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row_index - 1, col_index + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row_index):
            if row_index == n:
                res.append(["".join(r) for r in board])
                return

            for col_index in range(n):
                # Step 1: Find '.'
                # Step 2: Check valid
                # Step 3: Backtrack
                if board[row_index][col_index] == '.':
                    if isValid(row_index, col_index):
                        board[row_index][col_index] = 'Q'
                        backtrack(row_index + 1)
                        board[row_index][col_index] = '.'

        backtrack(0)
        return res


