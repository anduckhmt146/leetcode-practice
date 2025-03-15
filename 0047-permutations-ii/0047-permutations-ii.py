class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # Sort to handle duplicates
        used = [False] * len(nums)
        
        def dfs(start_index, path):
            if len(path) == len(nums):  # is_leaf condition
                ans.append(path[:])  # Add a copy of the path to results
                return
            
            for i in range(len(nums)):  # get_edges
                if used[i]:  # prune invalid edges
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # Skip duplicates
                
                path.append(nums[i])  # path.add(edge)
                used[i] = True  # update additional states
                
                dfs(start_index + 1, path)  # Recursive call
                
                path.pop()  # revert additional states
                used[i] = False
        
        dfs(0, [])
        return ans
