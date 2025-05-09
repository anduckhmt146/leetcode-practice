from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                res.append(path[:])
                return
            # [1,2], [1,3], [1,4]
            # When the i = 1 is pass, i = 2 and continue
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return res
