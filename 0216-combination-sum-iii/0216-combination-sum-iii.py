class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        candidates.sort()
        result = set()

        def backtrack(remaining, start, path):
            if remaining == 0 and len(path) == k:
                result.add(tuple(path))  # Convert to tuple to store in set
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates (common and understand)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                # i + 1: each number can be used only once
                backtrack(remaining - candidates[i], i + 1, path) 
                path.pop()

        backtrack(n, 0, [])
        return [list(comb) for comb in result]  # Convert each tuple back to list
        