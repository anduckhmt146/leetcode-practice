# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val
            
            # If it's a leaf node, check if the path sum matches targetSum
            if not node.left and not node.right:
                return currentSum == targetSum
            
            # Continue DFS on left and right subtrees
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        
        return dfs(root, 0)
