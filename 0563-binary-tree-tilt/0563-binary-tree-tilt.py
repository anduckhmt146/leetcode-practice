# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        titl = 0
        
        def dfs(node):
            nonlocal titl

            # Step 1: Basecase
            if not node:
                return 0

            # Step 2: Prunning
        
            # Step 3: What node.val do
            # Calculate the left and right abs
            left = dfs(node.left)
            right = dfs(node.right)
            titl += abs(left - right)

            # Step 4: What left right do for node
            return left + right + node.val

        dfs(root)
        return titl


