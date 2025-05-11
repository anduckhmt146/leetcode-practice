# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, path):
            nonlocal total  # Declare nonlocal so we can modify 'total'
            if not node:
                return
            
            path.append(str(node.val))
            if not node.left and not node.right:
                total += int("".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            # Backtrack
            path.pop()

        
        dfs(root, [])
        return total
        