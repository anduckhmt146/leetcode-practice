        #               []
        #              /  \
        #           [1]    []
        #          /  \    /  \
        #      [1,2]  [1] [2]  []
        #      /  \   / \  / \  / \
        # [1,2,2] [1,2] [2,2] [2] [2] []

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            
            # Explore further elements to add to the current subset
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] in the subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack, remove nums[i] from the current subset
                path.pop()

        nums.sort()  # Sort the array to handle duplicates
        result = []
        backtrack(0, [])
        return result