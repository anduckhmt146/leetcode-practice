from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(N^3)
        # N = len(grid)
        # count = 0
        # for i in range(0, N):
        #     firstRow = tuple(grid[i]) # Row i
        #     secondCol = []
        #     for k in range(0, N):
        #         thirdCol = []
        #         for j in range(0, N):
        #             thirdCol.append(grid[j][k])
        #         secondCol.append(tuple(thirdCol))

        #     counterCol = Counter(secondCol)
        #     count += counterCol[firstRow]

        # return count

        n = len(grid)

        # Convert rows to tuples
        row_tuples = [tuple(row) for row in grid]

        # Convert columns to tuples using zip
        col_tuples = list(zip(*grid))

        print(row_tuples, col_tuples)

        # Count frequency of each column
        col_counter = Counter(col_tuples)

        # Count how many rows match columns
        count = 0
        for row in row_tuples:
            count += col_counter[row]

        return count
            
            
        