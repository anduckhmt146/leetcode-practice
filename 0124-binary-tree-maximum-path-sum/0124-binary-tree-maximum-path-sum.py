# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute max path sum *starting* from left/right, ignore negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Max path THROUGH this node = left + node.val + right
            self.max_sum = max(self.max_sum, node.val + left + right)

            # Return max gain from this node to parent
            # IDEA: In root, in left and right, we have multiple branches, we only select a branch to do this
            # Care about what we return in root and leaf, it is enough
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum

        