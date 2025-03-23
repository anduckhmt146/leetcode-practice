from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(start_index, path):
            if start_index == len(nums):  # Base case: reach the end
                ans.append(path[:])  # Add a copy of the path to results
                return
            
            # Decision to include nums[start_index]
            path.append(nums[start_index])
            dfs(start_index + 1, path)
            path.pop()
            
            # Decision to exclude nums[start_index]
            dfs(start_index + 1, path)

        dfs(0, [])  # Start DFS from index 0
        return ans
