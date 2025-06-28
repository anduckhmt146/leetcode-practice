class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(index, path, remainingSum):
            if remainingSum == 0:
                res.append(path[:])
                return

            if index == n or remainingSum < 0:
                return
    
            path.append(candidates[index])
            backtrack(index, path, remainingSum - candidates[index])
            path.pop()
            backtrack(index + 1, path, remainingSum)

        backtrack(0, [], target)
        return res
        