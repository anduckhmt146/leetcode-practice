# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Duyet het
        count = 0
        
        def dfs(node, prev_max_value):
            nonlocal count
            if not node:
                return

            prev_max_value = max(prev_max_value, node.val)
            if node.val == prev_max_value:
                count += 1
            
            dfs(node.left, prev_max_value)
            dfs(node.right, prev_max_value)

        dfs(root, root.val)
        return count


        