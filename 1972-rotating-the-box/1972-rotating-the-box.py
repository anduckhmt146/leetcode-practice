class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Step 1: Apply gravity before rotation (simulate rightward fall)
        for row in boxGrid:
            write = n - 1
            for col in reversed(range(n)):
                if row[col] == '*':
                    write = col - 1
                elif row[col] == '#':
                    row[col] = '.'
                    row[write] = '#'
                    write -= 1

        # Step 2: Rotate the boxGrid clockwise
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        return rotated
            