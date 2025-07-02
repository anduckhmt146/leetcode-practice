# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, total):
            if not node:
                return False

            # Calculate sum until val
            total += node.val

            # Only check when find in a leaf node
            if not node.left and not node.right:
                return total == targetSum

            left = dfs(node.left, total)
            right = dfs(node.right, total)
            return left or right

        return dfs(root, 0)
            


        
