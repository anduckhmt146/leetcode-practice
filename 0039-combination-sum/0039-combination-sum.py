class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, path, currSum):
            # Base case
            if currSum == 0:
                result.append(path[:])
                return

            # Prunning
            if index == len(candidates) or currSum < 0:
                return

            # Neighbor
            for i in range(index, len(candidates)):
                # Node
                path.append(candidates[i])
                currSum -= candidates[i]
                backtrack(i, path, currSum)
                
                # Backtrack
                path.pop()
                currSum += candidates[i]
        
        backtrack(0, [], target)
        return result
