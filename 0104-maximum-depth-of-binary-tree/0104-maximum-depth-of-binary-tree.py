# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_height = 0

        # def dfs(node):
        #     if not node:
        #         return 0
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     return 1 + max(left, right)

        def dfs(node, depth):
            if not node:
                return

            self.max_height = max(self.max_height, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.max_height
        