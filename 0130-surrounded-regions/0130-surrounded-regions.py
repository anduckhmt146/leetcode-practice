class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def isValid(row_index, col_index):
            return 0 <= row_index < row and 0 <= col_index < col and not visited[row_index][col_index]

        def dfs(row_index, col_index):
            if not isValid(row_index, col_index) or board[row_index][col_index] != "O":
                return
            
            # Visited it
            board[row_index][col_index] = "#" 
            visited[row_index][col_index] = True

            # DFS without backtrack
            dfs(row_index + 1, col_index)
            dfs(row_index - 1, col_index)
            dfs(row_index, col_index + 1)
            dfs(row_index, col_index - 1)

        # DFS in borders
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)


        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
