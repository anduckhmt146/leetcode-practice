class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(0, numRows):
            result = [1] * (i + 1) # 1,2,3,4,5,...
            for j in range(1, len(result) - 1):
                if i < 2:
                    continue
                result[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(result)
        return triangle