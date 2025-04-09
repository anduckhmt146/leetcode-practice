class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining: int, combo: List[int], start: int):
            if remaining == 0:
                # If the remaining sum is 0, we found a valid combination
                result.append(list(combo))
                return
            elif remaining < 0:
                # If the remaining sum is negative, the combination is invalid
                return

            for i in range(start, len(candidates)):
                # Include the candidate number in the combination
                combo.append(candidates[i])
                # Recurse with the updated remaining sum and the same start index
                backtrack(remaining - candidates[i], combo, i)
                # Backtrack by removing the last added number
                combo.pop()

        result = []
        backtrack(target, [], 0)
        return result