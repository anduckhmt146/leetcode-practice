from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(N^3)
        N = len(grid)
        count = 0
        for i in range(0, N):
            firstRow = tuple(grid[i]) # Row i
            secondCol = []
            for k in range(0, N):
                thirdCol = []
                for j in range(0, N):
                    thirdCol.append(grid[j][k])
                secondCol.append(tuple(thirdCol))

            counterCol = Counter(secondCol)
            count += counterCol[firstRow]

        return count
            
            
        