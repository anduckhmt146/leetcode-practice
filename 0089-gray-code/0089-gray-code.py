from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):  # 2^n combinations
            result.append(i ^ (i >> 1))
        return result
